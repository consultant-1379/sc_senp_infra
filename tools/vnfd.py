#!/usr/bin/python3

import argparse
import datetime
import os
import sys
import uuid


def replace_value(orig_value, new_value, file):
    if file == 'vnfd':
        file_to_update = os.getcwd() + "/.bob/package/senp_infra.yaml"
    elif file == 'manifest':
        file_to_update = os.getcwd() + "/.bob/package/senp_infra-manifest.yaml"
    with open(file_to_update, "r") as ftu:
        data = ftu.read()
        # replace all occurrences of the orig_value string to new_value
        data = data.replace(orig_value, new_value)
    with open(file_to_update, "w") as ftu:
        ftu.write(data)

def update_descriptor_id():
    orig_value = '<current-descriptor_id>'
    new_value = str(uuid.uuid4())
    replace_value(orig_value, new_value, 'vnfd')
    #replace_value(orig_value, new_value, 'manifest')

def update_date_time():
    orig_value = '<current-date_time>'
    replace_value(orig_value, str(datetime.datetime.now().isoformat()), 'manifest')

def update_descriptor_version():
    orig_version = '<current-descriptor_version>'
    with open(os.getcwd() + "/.bob/var.major", "r") as f:
        major = f.read().strip()
    with open(os.getcwd() + "/.bob/var.r-state", "r") as f:
        r_state = f.read().strip()
    new_value = 'CXP9043136/'+ major + '_' + r_state
    replace_value(orig_version, new_value, 'vnfd')
    replace_value(orig_version, new_value, 'manifest')

def update_sw_version():
    orig_version = '<senp-infra-software_version>'
    with open(os.getcwd() + "/.bob/var.int-chart-version", "r") as f:
        version = f.read().strip()
    replace_value(orig_version, version, 'vnfd')

def get_senp_infra_ihc_file_name():
    crd_file_name = ''
    with open(os.getcwd() + "/.bob/var.int-chart-version", "r") as f:
        version = f.read().strip()
    with open(os.getcwd() + "/.bob/var.int-chart-name", "r") as f:
        file_name = f.read().strip()
    crd_file_name += '{file_name}-{version}.tgz'.format(file_name=file_name, version=version)
    return crd_file_name

def get_cn_base_file_name():
    base_helm_file_name = 'eric-cloud-native-base'
    with open(os.getcwd() + "/.bob/var.cncs-base-version", "r") as f:
        version = f.read().strip()
    base_helm_file_name += '-{version}.tgz'.format(version=version)
    return base_helm_file_name

def update_sc_senp_infra_artifact():
    orig_senp_infra = '<eric-clc-snia>'
    crd_file_name = get_senp_infra_ihc_file_name()
    replace_value(orig_senp_infra, crd_file_name, 'vnfd')

def update_cn_base_artifact():
    orig_cn_base = '<eric-cn-base>'
    base_helm_file_name = get_cn_base_file_name()
    replace_value(orig_cn_base, base_helm_file_name, 'vnfd')

def update_senp_infra_crd_artifact():
    orig_infra_crd = '<eric-tm-senp-infra-crd>'
    infra_crd_file_name = ''
    packages_dir = os.getcwd() + "/.bob/package"
    for dir_item in os.listdir(packages_dir):
        item_path = os.path.join(packages_dir, dir_item)
        if (os.path.isfile(item_path) and os.path.splitext(dir_item)[-1].find('tgz') != -1
                and os.path.splitext(dir_item)[0].find('-senp-infra-') != -1):
            infra_crd_file_name = dir_item
            break
    if infra_crd_file_name:
        replace_value(orig_infra_crd, infra_crd_file_name, 'vnfd')
    else:
        raise(ValueError('Could no find infra_crd file for {}.'.format(orig_infra_crd)))

def update_sec_sip_tls_crd_artifact():
    orig_tls_crd = '<eric-sec-sip-tls-crd>'
    tls_crd_file_name = ''
    packages_dir = os.getcwd() + "/.bob/package"
    for dir_item in os.listdir(packages_dir):
        item_path = os.path.join(packages_dir, dir_item)
        if (os.path.isfile(item_path) and os.path.splitext(dir_item)[-1].find('tgz') != -1
                and os.path.splitext(dir_item)[0].find('-tls-') != -1):
            tls_crd_file_name = dir_item
            break
    if tls_crd_file_name:
        replace_value(orig_tls_crd, tls_crd_file_name, 'vnfd')
    else:
        raise(ValueError('Could no find tls_crd file for {}.'.format(orig_tls_crd)))

def update_document_db_pg_crd_artifact():
    orig_document_db_pg_crd = '<eric-data-document-database-pg-crd>'
    document_database_pg_crd_file_name = ''
    packages_dir = os.getcwd() + "/.bob/package"
    for dir_item in os.listdir(packages_dir):
        item_path = os.path.join(packages_dir, dir_item)
        if (os.path.isfile(item_path) and os.path.splitext(dir_item)[-1].find('tgz') != -1
                and os.path.splitext(dir_item)[0].find('-database-pg-') != -1):
            document_database_pg_crd_file_name = dir_item
            break
    if document_database_pg_crd_file_name:
        replace_value(orig_document_db_pg_crd, document_database_pg_crd_file_name, 'vnfd')
    else:
        raise(ValueError('Could no find document_database_pg_crd file for {}.'.format(orig_document_db_pg_crd)))

def main():
    parser = argparse.ArgumentParser(description="Update VNF descriptor of SENP Infra")
    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.add_parser("vnfd_id", help="Updates descriptor_id")
    subparsers.add_parser("vnfd_version", help="Updates descriptor_version")
    subparsers.add_parser("sw_version", help="Updates dsc_software_version")
    subparsers.add_parser("date_time", help="Updates date_time")
    subparsers.add_parser("cn_base", help="Updates cn_base artifact")
    subparsers.add_parser("senp_infra_crd", help="Updates senp_infra_crd artifact")
    subparsers.add_parser("senp_infra", help="Updates senp_infra artifact")
    subparsers.add_parser("sip_tls_crd", help="Updates sip_tls_crd artifact")
    subparsers.add_parser("document_db_pg_crd", help="Updates document_db_pg_crd artifact")

    args = parser.parse_args()

    if args.subcommand == "vnfd_id":
        update_descriptor_id()
    elif args.subcommand == "vnfd_version":
        update_descriptor_version()
    elif args.subcommand == "sw_version":
        update_sw_version()
    elif args.subcommand == "date_time":
        update_date_time()
    elif args.subcommand == "cn_base":
        update_cn_base_artifact()
    elif args.subcommand == "senp_infra_crd":
        update_senp_infra_crd_artifact()
    elif args.subcommand == "senp_infra":
        update_sc_senp_infra_artifact()
    elif args.subcommand == "sip_tls_crd":
        update_sec_sip_tls_crd_artifact()
    elif args.subcommand == "document_db_pg_crd":
        update_document_db_pg_crd_artifact()
    else:
        sys.exit("Invalid subcommand")

if __name__ == "__main__":
    main()
