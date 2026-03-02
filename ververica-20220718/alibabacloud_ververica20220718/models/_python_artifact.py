# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PythonArtifact(DaraModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        additional_python_archives: List[str] = None,
        additional_python_libraries: List[str] = None,
        entry_module: str = None,
        main_args: str = None,
        python_artifact_uri: str = None,
    ):
        # The URL of the additional dependency file.
        self.additional_dependencies = additional_dependencies
        # The Python archive file on which the deployment depends.
        self.additional_python_archives = additional_python_archives
        # The Python library file on which the deployment depends.
        self.additional_python_libraries = additional_python_libraries
        # The startup module for the Python deployment.
        self.entry_module = entry_module
        # The startup parameter.
        self.main_args = main_args
        # The full URL for the Python deployment.
        self.python_artifact_uri = python_artifact_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies

        if self.additional_python_archives is not None:
            result['additionalPythonArchives'] = self.additional_python_archives

        if self.additional_python_libraries is not None:
            result['additionalPythonLibraries'] = self.additional_python_libraries

        if self.entry_module is not None:
            result['entryModule'] = self.entry_module

        if self.main_args is not None:
            result['mainArgs'] = self.main_args

        if self.python_artifact_uri is not None:
            result['pythonArtifactUri'] = self.python_artifact_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')

        if m.get('additionalPythonArchives') is not None:
            self.additional_python_archives = m.get('additionalPythonArchives')

        if m.get('additionalPythonLibraries') is not None:
            self.additional_python_libraries = m.get('additionalPythonLibraries')

        if m.get('entryModule') is not None:
            self.entry_module = m.get('entryModule')

        if m.get('mainArgs') is not None:
            self.main_args = m.get('mainArgs')

        if m.get('pythonArtifactUri') is not None:
            self.python_artifact_uri = m.get('pythonArtifactUri')

        return self

