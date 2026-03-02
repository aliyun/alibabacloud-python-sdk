# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class JarArtifact(DaraModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        entry_class: str = None,
        jar_uri: str = None,
        main_args: str = None,
    ):
        # The full URL of the additional dependency file. You can enter the dependency file for the JAR deployment.
        self.additional_dependencies = additional_dependencies
        # The entry class. You must enter the full name of the class.
        self.entry_class = entry_class
        # The full URL for the JAR deployment.
        self.jar_uri = jar_uri
        # The parameters required by the entry class.
        self.main_args = main_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies

        if self.entry_class is not None:
            result['entryClass'] = self.entry_class

        if self.jar_uri is not None:
            result['jarUri'] = self.jar_uri

        if self.main_args is not None:
            result['mainArgs'] = self.main_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')

        if m.get('entryClass') is not None:
            self.entry_class = m.get('entryClass')

        if m.get('jarUri') is not None:
            self.jar_uri = m.get('jarUri')

        if m.get('mainArgs') is not None:
            self.main_args = m.get('mainArgs')

        return self

