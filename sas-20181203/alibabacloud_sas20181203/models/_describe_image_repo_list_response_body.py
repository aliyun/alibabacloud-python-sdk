# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageRepoListResponseBody(DaraModel):
    def __init__(
        self,
        add_target_count: int = None,
        all_target_count: int = None,
        del_target_count: int = None,
        image_repo_list: List[main_models.DescribeImageRepoListResponseBodyImageRepoList] = None,
        page_info: main_models.DescribeImageRepoListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The number of image repositories that are added to Security Center.
        self.add_target_count = add_target_count
        # The total number of image repositories.
        self.all_target_count = all_target_count
        # The number of excluded image repositories.
        self.del_target_count = del_target_count
        # An array that consists of the information about image repositories.
        self.image_repo_list = image_repo_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_repo_list:
            for v1 in self.image_repo_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_target_count is not None:
            result['AddTargetCount'] = self.add_target_count

        if self.all_target_count is not None:
            result['AllTargetCount'] = self.all_target_count

        if self.del_target_count is not None:
            result['DelTargetCount'] = self.del_target_count

        result['ImageRepoList'] = []
        if self.image_repo_list is not None:
            for k1 in self.image_repo_list:
                result['ImageRepoList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTargetCount') is not None:
            self.add_target_count = m.get('AddTargetCount')

        if m.get('AllTargetCount') is not None:
            self.all_target_count = m.get('AllTargetCount')

        if m.get('DelTargetCount') is not None:
            self.del_target_count = m.get('DelTargetCount')

        self.image_repo_list = []
        if m.get('ImageRepoList') is not None:
            for k1 in m.get('ImageRepoList'):
                temp_model = main_models.DescribeImageRepoListResponseBodyImageRepoList()
                self.image_repo_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageRepoListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageRepoListResponseBodyPageInfo(DaraModel):
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

class DescribeImageRepoListResponseBodyImageRepoList(DaraModel):
    def __init__(
        self,
        flag: str = None,
        image_count: int = None,
        repo_name: str = None,
        repo_namespace: str = None,
    ):
        # Indicates whether the feature takes effect on the image repository. Valid values:
        # 
        # *   **add**: yes
        # *   **del**: no
        self.flag = flag
        # Number of images.
        self.image_count = image_count
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flag is not None:
            result['Flag'] = self.flag

        if self.image_count is not None:
            result['ImageCount'] = self.image_count

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        return self

