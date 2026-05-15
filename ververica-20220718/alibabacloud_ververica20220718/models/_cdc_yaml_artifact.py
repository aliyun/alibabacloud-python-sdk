# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CdcYamlArtifact(DaraModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        cdc_yaml: str = None,
    ):
        self.additional_dependencies = additional_dependencies
        self.cdc_yaml = cdc_yaml

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies

        if self.cdc_yaml is not None:
            result['cdcYaml'] = self.cdc_yaml

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')

        if m.get('cdcYaml') is not None:
            self.cdc_yaml = m.get('cdcYaml')

        return self

