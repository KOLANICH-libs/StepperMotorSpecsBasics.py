StepperMotorSpecsBasics.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
==========================
~~[wheel (GitLab)](https://gitlab.com/KOLANICH-libs/StepperMotorSpecsBasics.py/-/jobs/artifacts/master/raw/dist/StepperMotorSpecsBasics-0.CI-py3-none-any.whl?job=build)~~
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/StepperMotorSpecsBasics.py/workflows/CI/master/StepperMotorSpecsBasics-0.CI-py3-none-any.whl)~~
~~![GitLab Build Status](https://gitlab.com/KOLANICH-libs/StepperMotorSpecsBasics.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH-libs/StepperMotorSpecsBasics.py/badges/master/coverage.svg)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/StepperMotorSpecsBasics.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/StepperMotorSpecsBasics.py/actions/)~~
![N∅ dependencies](https://shields.io/badge/-N∅_deps!-0F0)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/StepperMotorSpecsBasics.py.svg)](https://libraries.io/github/KOLANICH-libs/StepperMotorSpecsBasics.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KOLANICH-libs/StepperMotorSpecsBasics.py, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

Just a lib encoding some basic relationships between stepper motor specifications.

There are different kinds of stepper motors:

* bipolar - have 2 windings (so - 4 wires), each must be driven by bipolar voltage.
* unipolar - have 4 windings connected sequentially, so they make 2 windings of bipolar with a central tap, so 6 wires. Can be driven with unipolar voltage.
* 8-wire - each subwinding of unipolar have distinct leads, so user can configure the motor. In addition to unipolar and bipolar driving modes bipolar parallel driving mode is available, when the subwindings are connected parallely.

This package allows you to encode some motor parameters in a standardized form (we use the params for bipolar driving mode as the most basic one) and compute them for the rest of driving modes.
