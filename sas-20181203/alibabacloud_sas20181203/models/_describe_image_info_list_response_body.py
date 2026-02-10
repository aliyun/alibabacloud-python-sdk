# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageInfoListResponseBody(DaraModel):
    def __init__(
        self,
        image_infos: List[main_models.DescribeImageInfoListResponseBodyImageInfos] = None,
        request_id: str = None,
    ):
        # An array that consists of the information about images.
        self.image_infos = image_infos
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_infos:
            for v1 in self.image_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageInfos'] = []
        if self.image_infos is not None:
            for k1 in self.image_infos:
                result['ImageInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_infos = []
        if m.get('ImageInfos') is not None:
            for k1 in m.get('ImageInfos'):
                temp_model = main_models.DescribeImageInfoListResponseBodyImageInfos()
                self.image_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageInfoListResponseBodyImageInfos(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        alarm_status: str = None,
        digest: str = None,
        endpoints: str = None,
        image_create: int = None,
        image_id: str = None,
        image_size: int = None,
        image_update: int = None,
        instance_id: str = None,
        region_id: str = None,
        registry_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_type: str = None,
        risk_status: str = None,
        source_biz_tag: str = None,
        status: str = None,
        tag: str = None,
        tag_immutable: int = None,
        uuid: str = None,
        vul_count: int = None,
        vul_status: str = None,
    ):
        # The number of alerts that are generated on the current pod, application, namespace, or cluster.
        self.alarm_count = alarm_count
        # Indicates whether alerts are generated on the asset. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.alarm_status = alarm_status
        # The digest value of the image.
        self.digest = digest
        # The endpoint of Container Registry.
        self.endpoints = endpoints
        # The time when the image was created.
        self.image_create = image_create
        # The ID of the image.
        self.image_id = image_id
        # The size of the image.
        self.image_size = image_size
        # The time when the image was updated.
        self.image_update = image_update
        # The ID of the image instance.
        self.instance_id = instance_id
        # The region ID of the image instance.
        self.region_id = region_id
        # The type of the registration.
        self.registry_type = registry_type
        # The ID of the image repository.
        self.repo_id = repo_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The type of the image repository. Valid values:
        # 
        # *   `PUBLIC`
        # *   `PRIVATE`
        self.repo_type = repo_type
        # Indicates whether the image is at risk. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.risk_status = risk_status
        # The usage label of the image.
        self.source_biz_tag = source_biz_tag
        # The status of the image.
        self.status = status
        # The tag that is added to the image.
        self.tag = tag
        # The tag immutability.
        self.tag_immutable = tag_immutable
        # The UUID of the server.
        self.uuid = uuid
        # The total number of vulnerabilities in your assets.
        self.vul_count = vul_count
        # Indicates whether vulnerabilities are detected on the asset. Valid values:
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

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints

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

        if self.source_biz_tag is not None:
            result['SourceBizTag'] = self.source_biz_tag

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tag_immutable is not None:
            result['TagImmutable'] = self.tag_immutable

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

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('Endpoints') is not None:
            self.endpoints = m.get('Endpoints')

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

        if m.get('SourceBizTag') is not None:
            self.source_biz_tag = m.get('SourceBizTag')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TagImmutable') is not None:
            self.tag_immutable = m.get('TagImmutable')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')

        return self

