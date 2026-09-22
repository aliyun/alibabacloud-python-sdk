# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetAiAppDetailTopoResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetAiAppDetailTopoResponseBodyData] = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetAiAppDetailTopoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAiAppDetailTopoResponseBodyData(DaraModel):
    def __init__(
        self,
        node_category: str = None,
        node_id: str = None,
        node_name: str = None,
        node_type: str = None,
        request_count: int = None,
        risk_level: str = None,
        warning_count: int = None,
    ):
        # The node category.
        # 
        # - LLM
        # 
        # - Knowledge
        # 
        # - Tools
        # 
        # - Others
        self.node_category = node_category
        # The node ID.
        self.node_id = node_id
        # The node name.
        self.node_name = node_name
        # The node type. Valid values:
        # 
        # - **APP**: end-to-end agent.
        # - **MODEL**: large language model.
        # - **TOOL**: tool.
        self.node_type = node_type
        # The request count.
        self.request_count = request_count
        # The risk level.
        self.risk_level = risk_level
        # The alert count.
        self.warning_count = warning_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_category is not None:
            result['NodeCategory'] = self.node_category

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCategory') is not None:
            self.node_category = m.get('NodeCategory')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')

        return self

