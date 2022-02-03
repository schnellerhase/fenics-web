"""Test governance pages."""

import os
import github


def test_governance_institutions():
    """Test that the list of institutions agrees with governance repo."""
    with open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "../governance/index.md"
    )) as f:
        content = f.read()
    partners = set(
        i.split("]")[0]
        for i in content.split("[![")[1:])
    partners.remove("NumFOCUS")

    git = github.Github()

    gov = git.get_repo("fenics/governance")
    content = gov.get_contents("people.md").decoded_content.decode("utf8")
    content = content.split("## Institutional Partners")[1].split("##")[0]
    partners2 = set(
        i.split("]")[0]
        for i in content.split("- [")[1:])

    assert partners == partners2
