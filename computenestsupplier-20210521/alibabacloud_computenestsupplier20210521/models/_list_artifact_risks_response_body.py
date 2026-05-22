# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListArtifactRisksResponseBody(DaraModel):
    def __init__(
        self,
        artifact_risk_list: List[main_models.ListArtifactRisksResponseBodyArtifactRiskList] = None,
        request_id: str = None,
    ):
        # List of artifact risks
        self.artifact_risk_list = artifact_risk_list
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.artifact_risk_list:
            for v1 in self.artifact_risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ArtifactRiskList'] = []
        if self.artifact_risk_list is not None:
            for k1 in self.artifact_risk_list:
                result['ArtifactRiskList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.artifact_risk_list = []
        if m.get('ArtifactRiskList') is not None:
            for k1 in m.get('ArtifactRiskList'):
                temp_model = main_models.ListArtifactRisksResponseBodyArtifactRiskList()
                self.artifact_risk_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListArtifactRisksResponseBodyArtifactRiskList(DaraModel):
    def __init__(
        self,
        cve_nos: str = None,
        extend_info: str = None,
        level: str = None,
        risk_name: str = None,
        risk_type: str = None,
        risk_type_name: str = None,
        solution: str = None,
    ):
        # CVE numbers
        self.cve_nos = cve_nos
        # Extended information, in JSON format, to be parsed according to the risk category
        self.extend_info = extend_info
        # Risk level:
        # 
        # - high represents high
        self.level = level
        # Risk name.
        self.risk_name = risk_name
        # Risk type. Values:
        # - AcrCve  Container image system vulnerability
        # - AcrSca  Container image application vulnerability
        # - EcsVulnerability  ECS image vulnerability information
        # - EcsAlarm  ECS image security alarm
        # - EcsBaseline  ECS image baseline check
        self.risk_type = risk_type
        # Risk Type name
        self.risk_type_name = risk_type_name
        # Solution for the risk item.
        self.solution = solution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_nos is not None:
            result['CveNos'] = self.cve_nos

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.level is not None:
            result['Level'] = self.level

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        if self.risk_type_name is not None:
            result['RiskTypeName'] = self.risk_type_name

        if self.solution is not None:
            result['Solution'] = self.solution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveNos') is not None:
            self.cve_nos = m.get('CveNos')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        if m.get('RiskTypeName') is not None:
            self.risk_type_name = m.get('RiskTypeName')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        return self

