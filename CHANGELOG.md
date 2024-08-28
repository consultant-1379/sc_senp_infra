# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- eric-tm-senp-infra sub-chart dependency changes
    - New released PRA version
    - CNCS-base version change from 1.0.0+6 to 1.1.0-190
- Change the Jenkins job currentBuild.displayName from "BUILD_NUMBER - VERSION"
  to "BUILD_NUMBER VERSION" (without dash)

### Fixed

- Avoid printout of ~/.artifactory/helm_repositories.yaml contents
- Fix timeout in all Jenkins jobs
    - inca timeout after some retries, so prepare and publish jenkinsfile scripts
    should allow some retries but not more than 15 minutes
    - decision related jenkinsfile scripts should timeout after 2 minutes
- Fix and align parameter (eg GIT_REPO_URL, CHART_NAME, CHART_VERSION)
description in all jenkinsfile scripts

## [pra/1.1.0] - 2023-02-20

### Changed

- eric-cloud-native-base sub-chart dependency changes
    - New released PRA version
    - CNCS-base version change from 93.4.0 to 93.5.0

## [pra/1.0.0] - 2023-02-20

### Added

- Initial infra repository structure
- New Jenkins jobs to be used for generation of new infra integration charts
- New ruleset yaml files to be used by bob framework from the Jenkins jobs
- Automation uses INCA tool that performs the generation of new integration charts,
including their upload in internal/drop/released helm repositories.
- Current infra integration chart dependencies:
    - eric-tm-senp-infra
    - eric-cloud-native-base
    - eric-data-document-database-pg

### Changed

- No changes to record, first PRA version

### Deprecated

- eric-cloud-native-base sub-chart dependency should be removed and it should be
installed separately before infra integration chart

### Removed

- No features or functions removed, first PRA version

### Fixed

- Nothing to fix, first PRA version

### Security

- No vulnerabilities to record, first PRA version
- Vulnerabilities come from sub-chart dependencies

[unreleased]: https://gerrit.ericsson.se/plugins/gitiles/MC_5G/sc_senp_infra/+/pra/1.1.0..HEAD
[pra/1.1.0]: https://gerrit.ericsson.se/plugins/gitiles/MC_5G/sc_senp_infra/+/pra/1.0.0..1.1.0
[pra/1.0.0]: https://gerrit.ericsson.se/plugins/gitiles/MC_5G/sc_senp_infra/+/pra/1.0.0
