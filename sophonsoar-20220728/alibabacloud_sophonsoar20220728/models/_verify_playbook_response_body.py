# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class VerifyPlaybookResponseBody(DaraModel):
    def __init__(
        self,
        check_task_infos: List[main_models.VerifyPlaybookResponseBodyCheckTaskInfos] = None,
        prerequisites: List[main_models.VerifyPlaybookResponseBodyPrerequisites] = None,
        request_id: str = None,
    ):
        # The result of the verification.
        self.check_task_infos = check_task_infos
        self.prerequisites = prerequisites
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_task_infos:
            for v1 in self.check_task_infos:
                 if v1:
                    v1.validate()
        if self.prerequisites:
            for v1 in self.prerequisites:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckTaskInfos'] = []
        if self.check_task_infos is not None:
            for k1 in self.check_task_infos:
                result['CheckTaskInfos'].append(k1.to_map() if k1 else None)

        result['Prerequisites'] = []
        if self.prerequisites is not None:
            for k1 in self.prerequisites:
                result['Prerequisites'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_task_infos = []
        if m.get('CheckTaskInfos') is not None:
            for k1 in m.get('CheckTaskInfos'):
                temp_model = main_models.VerifyPlaybookResponseBodyCheckTaskInfos()
                self.check_task_infos.append(temp_model.from_map(k1))

        self.prerequisites = []
        if m.get('Prerequisites') is not None:
            for k1 in m.get('Prerequisites'):
                temp_model = main_models.VerifyPlaybookResponseBodyPrerequisites()
                self.prerequisites.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class VerifyPlaybookResponseBodyPrerequisites(DaraModel):
    def __init__(
        self,
        prerequisite_type: str = None,
        prerequisite_value: str = None,
    ):
        self.prerequisite_type = prerequisite_type
        self.prerequisite_value = prerequisite_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prerequisite_type is not None:
            result['PrerequisiteType'] = self.prerequisite_type

        if self.prerequisite_value is not None:
            result['PrerequisiteValue'] = self.prerequisite_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrerequisiteType') is not None:
            self.prerequisite_type = m.get('PrerequisiteType')

        if m.get('PrerequisiteValue') is not None:
            self.prerequisite_value = m.get('PrerequisiteValue')

        return self

class VerifyPlaybookResponseBodyCheckTaskInfos(DaraModel):
    def __init__(
        self,
        detail: str = None,
        node_name: str = None,
        risk_level: str = None,
    ):
        # The error message returned when the playbook does not pass the check.
        self.detail = detail
        # The name of the node in the playbook.
        self.node_name = node_name
        # The severity level of the verification information. Valid values:
        # 
        # *   warn: An issue may occur during playbook running.
        # *   error: The playbook cannot be compiled.
        # *   remind: The publishing and running of the playbook are not affected. We recommend that you optimize the playbook format.
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

