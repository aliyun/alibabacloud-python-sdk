# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeExecutePlaybooksResponseBody(DaraModel):
    def __init__(
        self,
        playbook_metrics: List[main_models.DescribeExecutePlaybooksResponseBodyPlaybookMetrics] = None,
        request_id: str = None,
    ):
        # The playbook.
        self.playbook_metrics = playbook_metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbook_metrics:
            for v1 in self.playbook_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PlaybookMetrics'] = []
        if self.playbook_metrics is not None:
            for k1 in self.playbook_metrics:
                result['PlaybookMetrics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.playbook_metrics = []
        if m.get('PlaybookMetrics') is not None:
            for k1 in m.get('PlaybookMetrics'):
                temp_model = main_models.DescribeExecutePlaybooksResponseBodyPlaybookMetrics()
                self.playbook_metrics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeExecutePlaybooksResponseBodyPlaybookMetrics(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        param_config: str = None,
        param_type: str = None,
        uuid: str = None,
    ):
        # The playbook description.
        self.description = description
        # The playbook name.
        self.display_name = display_name
        # The configuration of the input parameter. The value is a JSON array.
        # 
        # >  For more information, see [DescribePlaybookInputOutput](~~DescribePlaybookInputOutput~~).
        self.param_config = param_config
        # The input parameter type of the playbook.
        # 
        # *   **template-ip**
        # *   **template-file**
        # *   **template-process**
        # *   **custom**
        self.param_type = param_type
        # The playbook UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.param_config is not None:
            result['ParamConfig'] = self.param_config

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ParamConfig') is not None:
            self.param_config = m.get('ParamConfig')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

