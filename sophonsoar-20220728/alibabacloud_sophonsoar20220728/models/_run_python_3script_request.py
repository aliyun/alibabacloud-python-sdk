# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunPython3ScriptRequest(DaraModel):
    def __init__(
        self,
        node_name: str = None,
        params: str = None,
        playbook_uuid: str = None,
        python_script: str = None,
        python_version: str = None,
    ):
        # The name of the node in the playbook.
        self.node_name = node_name
        # The input parameters of the Python3 script.
        self.params = params
        # The UUID of the playbook.
        # 
        # >  You can call the [DescribePlaybooks](~~DescribePlaybooks~~) operation to query the UUIDs of playbooks.
        self.playbook_uuid = playbook_uuid
        # The Python3 script.
        self.python_script = python_script
        self.python_version = python_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.params is not None:
            result['Params'] = self.params

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.python_script is not None:
            result['PythonScript'] = self.python_script

        if self.python_version is not None:
            result['PythonVersion'] = self.python_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('PythonScript') is not None:
            self.python_script = m.get('PythonScript')

        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')

        return self

