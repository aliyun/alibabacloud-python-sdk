# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetDockerhubImageRiskRankInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_rank_info: main_models.GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The risk information.
        self.risk_rank_info = risk_rank_info

    def validate(self):
        if self.risk_rank_info:
            self.risk_rank_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_rank_info is not None:
            result['RiskRankInfo'] = self.risk_rank_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskRankInfo') is not None:
            temp_model = main_models.GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfo()
            self.risk_rank_info = temp_model.from_map(m.get('RiskRankInfo'))

        return self

class GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfo(DaraModel):
    def __init__(
        self,
        baseline: List[main_models.GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfoBaseline] = None,
        vul_asap: List[main_models.GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfoVulAsap] = None,
    ):
        # The baseline risks.
        self.baseline = baseline
        # The risk information of high-risk vulnerabilities.
        self.vul_asap = vul_asap

    def validate(self):
        if self.baseline:
            for v1 in self.baseline:
                 if v1:
                    v1.validate()
        if self.vul_asap:
            for v1 in self.vul_asap:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Baseline'] = []
        if self.baseline is not None:
            for k1 in self.baseline:
                result['Baseline'].append(k1.to_map() if k1 else None)

        result['VulAsap'] = []
        if self.vul_asap is not None:
            for k1 in self.vul_asap:
                result['VulAsap'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline = []
        if m.get('Baseline') is not None:
            for k1 in m.get('Baseline'):
                temp_model = main_models.GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfoBaseline()
                self.baseline.append(temp_model.from_map(k1))

        self.vul_asap = []
        if m.get('VulAsap') is not None:
            for k1 in m.get('VulAsap'):
                temp_model = main_models.GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfoVulAsap()
                self.vul_asap.append(temp_model.from_map(k1))

        return self

class GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfoVulAsap(DaraModel):
    def __init__(
        self,
        digest: str = None,
        hc_count: int = None,
        image_id: str = None,
        image_size: int = None,
        repo_name: str = None,
        repo_namespace: str = None,
        risk_level_detail: str = None,
        tag: str = None,
        uuid: str = None,
        vul_count: int = None,
    ):
        # The digest value of the image.
        self.digest = digest
        # The number of risks detected on the image repository.
        self.hc_count = hc_count
        # The image ID.
        self.image_id = image_id
        # The image size.
        self.image_size = image_size
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The risk statistics of all hosts, images, and containers.
        self.risk_level_detail = risk_level_detail
        # The tag of the image.
        self.tag = tag
        # The UUID of the record.
        self.uuid = uuid
        # The number of vulnerabilities.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.risk_level_detail is not None:
            result['RiskLevelDetail'] = self.risk_level_detail

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RiskLevelDetail') is not None:
            self.risk_level_detail = m.get('RiskLevelDetail')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

class GetDockerhubImageRiskRankInfoResponseBodyRiskRankInfoBaseline(DaraModel):
    def __init__(
        self,
        digest: str = None,
        hc_count: int = None,
        image_id: str = None,
        image_size: int = None,
        repo_name: str = None,
        repo_namespace: str = None,
        risk_level_detail: str = None,
        tag: str = None,
        uuid: str = None,
        vul_count: int = None,
    ):
        # The digest value of the image.
        self.digest = digest
        # The number of baseline risks detected on the image repository.
        self.hc_count = hc_count
        # The ID of the image.
        self.image_id = image_id
        # The image size.
        self.image_size = image_size
        # The name of the Container Registry repository.
        self.repo_name = repo_name
        # The namespace to which the repository belongs.
        self.repo_namespace = repo_namespace
        # The risk statistics of all hosts, images, and containers.
        self.risk_level_detail = risk_level_detail
        # The tag of the image.
        self.tag = tag
        # The UUID of the record.
        self.uuid = uuid
        # The number of detected vulnerabilities.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.risk_level_detail is not None:
            result['RiskLevelDetail'] = self.risk_level_detail

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RiskLevelDetail') is not None:
            self.risk_level_detail = m.get('RiskLevelDetail')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

