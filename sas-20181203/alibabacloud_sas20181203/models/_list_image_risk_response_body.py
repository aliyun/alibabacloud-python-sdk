# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListImageRiskResponseBody(DaraModel):
    def __init__(
        self,
        image_risk_list: List[main_models.ListImageRiskResponseBodyImageRiskList] = None,
        page_info: main_models.ListImageRiskResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of security information about the image.
        self.image_risk_list = image_risk_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_risk_list:
            for v1 in self.image_risk_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageRiskList'] = []
        if self.image_risk_list is not None:
            for k1 in self.image_risk_list:
                result['ImageRiskList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_risk_list = []
        if m.get('ImageRiskList') is not None:
            for k1 in m.get('ImageRiskList'):
                temp_model = main_models.ListImageRiskResponseBodyImageRiskList()
                self.image_risk_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListImageRiskResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListImageRiskResponseBodyPageInfo(DaraModel):
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
        # The total number of entries returned.
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

class ListImageRiskResponseBodyImageRiskList(DaraModel):
    def __init__(
        self,
        digest: str = None,
        end_point_list: List[main_models.ListImageRiskResponseBodyImageRiskListEndPointList] = None,
        endpoints: str = None,
        image: str = None,
        image_access_type: str = None,
        image_id: str = None,
        internet_urls: str = None,
        region_id: str = None,
        registry_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_type: str = None,
        statistics: str = None,
        tag: str = None,
        tag_immutable: int = None,
        uuid: str = None,
        vpc_urls: str = None,
    ):
        # The digest value of the image.
        self.digest = digest
        # An array that consists of the details of the endpoint.
        self.end_point_list = end_point_list
        # The endpoint of Container Registry.
        self.endpoints = endpoints
        # The image of the container.
        self.image = image
        # The registration status of the image repository. Valid values:
        # 
        # *   **IN_SAS**: The image repository is registered with Security Center.
        # *   **NOT_IN_SAS**: The image repository is not registered with Security Center.
        self.image_access_type = image_access_type
        # The ID of the image.
        self.image_id = image_id
        # The public endpoint of the image repository.
        self.internet_urls = internet_urls
        # The region of the image repository.
        self.region_id = region_id
        # The type of the image repository. Valid values:
        # 
        # *   **acr**
        # *   **harbor**
        # *   **quay**
        # *   **CI/CD**: Jenkins
        self.registry_type = registry_type
        # The ID of the image repository.
        self.repo_id = repo_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace = repo_namespace
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`
        # *   `PRIVATE`
        self.repo_type = repo_type
        # The statistics on a security event.
        self.statistics = statistics
        # The tag that is added to the image.
        self.tag = tag
        # Indicates whether the image version is immutable. If the image version is immutable, only the image of the latest version in the image repository can be overwritten. Valid values:
        # 
        # *   **0**: The image version is mutable.
        # *   **1**: The image version is immutable.
        self.tag_immutable = tag_immutable
        # The UUID of the image.
        self.uuid = uuid
        # The endpoint of the image repository in the VPC.
        self.vpc_urls = vpc_urls

    def validate(self):
        if self.end_point_list:
            for v1 in self.end_point_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        result['EndPointList'] = []
        if self.end_point_list is not None:
            for k1 in self.end_point_list:
                result['EndPointList'].append(k1.to_map() if k1 else None)

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints

        if self.image is not None:
            result['Image'] = self.image

        if self.image_access_type is not None:
            result['ImageAccessType'] = self.image_access_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.internet_urls is not None:
            result['InternetURLs'] = self.internet_urls

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

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tag_immutable is not None:
            result['TagImmutable'] = self.tag_immutable

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_urls is not None:
            result['VpcURLs'] = self.vpc_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        self.end_point_list = []
        if m.get('EndPointList') is not None:
            for k1 in m.get('EndPointList'):
                temp_model = main_models.ListImageRiskResponseBodyImageRiskListEndPointList()
                self.end_point_list.append(temp_model.from_map(k1))

        if m.get('Endpoints') is not None:
            self.endpoints = m.get('Endpoints')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageAccessType') is not None:
            self.image_access_type = m.get('ImageAccessType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InternetURLs') is not None:
            self.internet_urls = m.get('InternetURLs')

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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TagImmutable') is not None:
            self.tag_immutable = m.get('TagImmutable')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcURLs') is not None:
            self.vpc_urls = m.get('VpcURLs')

        return self

class ListImageRiskResponseBodyImageRiskListEndPointList(DaraModel):
    def __init__(
        self,
        domains: List[str] = None,
        type: str = None,
    ):
        # An array that consists the details of the domain name in the endpoint.
        self.domains = domains
        # The type of the domain name in the endpoint. Valid values:
        # 
        # *   **internet**: Internet
        # *   **intranet**: internal network
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

