# SENP INFRA Application

[TOC]

## Description

This repository contains SENP INFRA application and all dependencies needed
for functions like TLS and backend postgress database.

## Contact

### Jira

Create new issue on DND project with label 5GC and assign to team sigchallengers:
Report [Bug][1]

### E-mail list

Send e-mail to [Challengers Team][2]

## Contributing

We are an inner source project and welcome contributions.
See our [Contributing Guide](CONTRIBUTING.md) for details.

## Documentation

* [Change Log](CHANGELOG.md)

### CI pipeline code

This repository includes pipeline code designed to run on a Jenkins slave.

* review pipeline
    * [pre-code-review](./jenkins/pre-code-review.jenkinsfile)
* prepare pipelines
    * [prepare-decision](./jenkins/prepare-decision.jenkinsfile)
    * [prepare](./jenkins/prepare.jenkinsfile)
* publish pipelines
    * [publish-decision](./jenkins/publish-decision.jenkinsfile)
    * [publish](./jenkins/publish.jenkinsfile)
* release pipeline
    * [pra](./jenkins/pra.jenkinsfile)

### Manual Execution

This repository utilizes CI Jenkins pipelines under the umbrella of
[SC-SENF-INFRA pipeline][3] spinnaker pipeline based on code review requests and
the generation of new integration charts performed automatically. The manual
execution of Jenkins jobs or rulesets is prohibited and it is mainly used by the
project guardians for troubleshooting purposes. If you would like to contibute,
please check [Contributing guide](CONTRIBUTING.md)

[1]: https://eteamproject.internal.ericsson.com/secure/CreateIssue.jspa?pid=33703&amp;issuetype=10203
[2]: mailto://IXG-ChallengersTeam@ericsson.onmicrosoft.com
[3]: https://spinnaker.rnd.gic.ericsson.se/#/applications/esc5gtest/executions?pipeline=SC-SENP-INFRA
