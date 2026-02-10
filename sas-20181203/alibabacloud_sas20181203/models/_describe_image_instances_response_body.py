# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageInstancesResponseBody(DaraModel):
    def __init__(
        self,
        image_instance_list: List[main_models.DescribeImageInstancesResponseBodyImageInstanceList] = None,
        page_info: main_models.DescribeImageInstancesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the images.
        self.image_instance_list = image_instance_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_instance_list:
            for v1 in self.image_instance_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageInstanceList'] = []
        if self.image_instance_list is not None:
            for k1 in self.image_instance_list:
                result['ImageInstanceList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_instance_list = []
        if m.get('ImageInstanceList') is not None:
            for k1 in m.get('ImageInstanceList'):
                temp_model = main_models.DescribeImageInstancesResponseBodyImageInstanceList()
                self.image_instance_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageInstancesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of images returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
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

class DescribeImageInstancesResponseBodyImageInstanceList(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        alarm_status: str = None,
        deployed: int = None,
        digest: str = None,
        endpoints: str = None,
        hc_count: int = None,
        hc_status: str = None,
        image_create: str = None,
        image_id: str = None,
        image_size: str = None,
        image_update: str = None,
        instance_id: str = None,
        last_scan_time: int = None,
        region_id: str = None,
        registry_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_type: str = None,
        risk_status: str = None,
        sca_progress: int = None,
        sca_result: str = None,
        sca_status: str = None,
        source_biz_tag: str = None,
        status: str = None,
        tag: str = None,
        uuid: str = None,
        vul_count: int = None,
        vul_status: str = None,
    ):
        # The number of alerts that are generated for the image.
        self.alarm_count = alarm_count
        # Indicates whether alerts are generated for the image. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.alarm_status = alarm_status
        # Indicates whether the image was deployed. Valid values:
        # 
        # *   **0**: The image was not deployed.
        # *   **1**: The image was deployed.
        self.deployed = deployed
        # The digest value of the image.
        self.digest = digest
        # The address of the image.
        self.endpoints = endpoints
        # The number of baseline risks.
        self.hc_count = hc_count
        # Indicates whether baseline risks exist. Valid values:
        # 
        # *   **NO**
        # *   **YES**
        self.hc_status = hc_status
        # The timestamp generated when the image was created. Unit: milliseconds.
        self.image_create = image_create
        # The ID of the image.
        self.image_id = image_id
        # The size of the image. Unit: MB.
        self.image_size = image_size
        # The timestamp generated when the image was updated. Unit: milliseconds.
        self.image_update = image_update
        # The instance ID of the image.
        self.instance_id = instance_id
        # The timestamp when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The region ID of the image.
        self.region_id = region_id
        # The type of the image. Valid values:
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
        # The type of the repository. Valid values:
        # 
        # *   **private**
        # *   **public**
        self.repo_type = repo_type
        # Indicates whether risks exist. Valid values:
        # 
        # *   **NO**
        # *   **YES**
        self.risk_status = risk_status
        # The scan progress of the image. Valid values: 0 to 100.
        self.sca_progress = sca_progress
        # The error code of the image scan result. Valid values:
        # 
        # *   **TASK_NOT_EXISTS**: The image scan task does not exist.
        # *   **TASK_NOT_SUPPORT_REGION**: The image scan task cannot be performed in the current region.
        # *   **forbid_create_repeat_task**: The image scan task already exists.
        self.sca_result = sca_result
        # The scan status of the image. Valid values:
        # 
        # *   **INIT**: The image scan task is pending startup.
        # *   **START**: The image scan task is started.
        # *   **MESSAGE_SEND**: The message about the image scan task is sent.
        # *   **START_RUN**: The image analysis task is started.
        # *   **DOWNLOAD**: The image scan result is downloaded.
        # *   **PRE_ANALYZER**: The image pre-analysis is started.
        # *   **WEB_SHELL_ANALYZER**: The WebShell analysis of the image is complete.
        # *   **CVE_ANALYZER**: The Common Vulnerabilities and Exposures (CVE) analysis of the image is complete.
        # *   **BIN_ANALYZER**: The binary analysis of the image is complete.
        # *   **OTHER_ANALYZER**: The extended analysis of the image is complete.
        # *   **SUCCESS**: The image scan task is complete.
        # *   **PRE_ANALYZER_SUCCESS**: The image pre-analysis is complete.
        # *   **FAIL**: The image scan task failed.
        # *   **TIMEOUT**: The image scan task timed out.
        self.sca_status = sca_status
        # The usage label of the image.
        self.source_biz_tag = source_biz_tag
        # The status of the image. Valid values:
        # 
        # *   **NORMAL**
        self.status = status
        # The tag of the image.
        self.tag = tag
        # The UUID of the server.
        self.uuid = uuid
        # The number of vulnerabilities in the image.
        self.vul_count = vul_count
        # Indicates whether vulnerabilities exist in the image. Valid values:
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

        if self.deployed is not None:
            result['Deployed'] = self.deployed

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.hc_status is not None:
            result['HcStatus'] = self.hc_status

        if self.image_create is not None:
            result['ImageCreate'] = self.image_create

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

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

        if self.repo_type is not None:
            result['RepoType'] = self.repo_type

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.sca_progress is not None:
            result['ScaProgress'] = self.sca_progress

        if self.sca_result is not None:
            result['ScaResult'] = self.sca_result

        if self.sca_status is not None:
            result['ScaStatus'] = self.sca_status

        if self.source_biz_tag is not None:
            result['SourceBizTag'] = self.source_biz_tag

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

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

        if m.get('Deployed') is not None:
            self.deployed = m.get('Deployed')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('Endpoints') is not None:
            self.endpoints = m.get('Endpoints')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('HcStatus') is not None:
            self.hc_status = m.get('HcStatus')

        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

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

        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('ScaProgress') is not None:
            self.sca_progress = m.get('ScaProgress')

        if m.get('ScaResult') is not None:
            self.sca_result = m.get('ScaResult')

        if m.get('ScaStatus') is not None:
            self.sca_status = m.get('ScaStatus')

        if m.get('SourceBizTag') is not None:
            self.source_biz_tag = m.get('SourceBizTag')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')

        return self

