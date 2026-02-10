# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageRepoDetailListResponseBody(DaraModel):
    def __init__(
        self,
        image_repo_responses: List[main_models.DescribeImageRepoDetailListResponseBodyImageRepoResponses] = None,
        page_info: main_models.DescribeImageRepoDetailListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about image repositories.
        self.image_repo_responses = image_repo_responses
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_repo_responses:
            for v1 in self.image_repo_responses:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageRepoResponses'] = []
        if self.image_repo_responses is not None:
            for k1 in self.image_repo_responses:
                result['ImageRepoResponses'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_repo_responses = []
        if m.get('ImageRepoResponses') is not None:
            for k1 in m.get('ImageRepoResponses'):
                temp_model = main_models.DescribeImageRepoDetailListResponseBodyImageRepoResponses()
                self.image_repo_responses.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageRepoDetailListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageRepoDetailListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of image repositories.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageRepoDetailListResponseBodyImageRepoResponses(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        alarm_status: str = None,
        endpoints: str = None,
        has_risk_image_count: int = None,
        hc_count: int = None,
        hc_status: str = None,
        image_count: int = None,
        instance_id: str = None,
        region_id: str = None,
        registry_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        risk_status: str = None,
        source_biz_tag: str = None,
        vul_count: int = None,
        vul_status: str = None,
    ):
        # The number of alerts that are generated for the image repository.
        self.alarm_count = alarm_count
        # Indicates whether alerts are generated for the image repository. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.alarm_status = alarm_status
        # The address of the image repository.
        self.endpoints = endpoints
        # The number of the images on which risks are detected.
        self.has_risk_image_count = has_risk_image_count
        # The number of baseline risk items on the image repository.
        self.hc_count = hc_count
        # Indicates whether baseline risk items are detected on the image repository. Valid values:
        # 
        # *   **NO**
        # *   **YES**
        self.hc_status = hc_status
        # The number of images.
        self.image_count = image_count
        # The ID of the image.
        self.instance_id = instance_id
        # The region ID of the image.
        self.region_id = region_id
        # The type of the image repository. Valid values:
        # 
        # *   **acr**
        # *   **harbor**
        # *   **quay**
        # *   **CI/CD**
        self.registry_type = registry_type
        # The ID of the image repository.
        self.repo_id = repo_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # Indicates whether the image repository is at risk. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.risk_status = risk_status
        # The usage label of the image.
        self.source_biz_tag = source_biz_tag
        # The number of vulnerabilities detected on the image repository.
        self.vul_count = vul_count
        # Indicates whether vulnerabilities are detected on the image repository. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.vul_status = vul_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints

        if self.has_risk_image_count is not None:
            result['HasRiskImageCount'] = self.has_risk_image_count

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.hc_status is not None:
            result['HcStatus'] = self.hc_status

        if self.image_count is not None:
            result['ImageCount'] = self.image_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.source_biz_tag is not None:
            result['SourceBizTag'] = self.source_biz_tag

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        if self.vul_status is not None:
            result['VulStatus'] = self.vul_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')

        if m.get('Endpoints') is not None:
            self.endpoints = m.get('Endpoints')

        if m.get('HasRiskImageCount') is not None:
            self.has_risk_image_count = m.get('HasRiskImageCount')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('HcStatus') is not None:
            self.hc_status = m.get('HcStatus')

        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('SourceBizTag') is not None:
            self.source_biz_tag = m.get('SourceBizTag')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')

        return self

