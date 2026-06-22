# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageRepoListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        field_name: str = None,
        field_value: str = None,
        operate_type: str = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace: str = None,
        selected: int = None,
        target_type: str = None,
        type: str = None,
    ):
        # The page number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The search field. Valid values:
        # 
        # - **repoName**: image repository name
        # - **repoNamespace**: image repository namespace
        # 
        # > This parameter takes effect only when **OperateType** is set to **other**.
        self.field_name = field_name
        # The value of the search field.
        # > This parameter takes effect only when **OperateType** is set to **other**.
        self.field_value = field_value
        # The operation type. Valid values:
        # 
        # - **count**: statistics
        # - **other**: other.
        self.operate_type = operate_type
        # The number of entries per page in a paged query. Default value: 20. If you leave this parameter empty, 20 entries are returned per page during paging.
        # > Set PageSize to a non-empty value.
        self.page_size = page_size
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace of the container image repository.
        self.repo_namespace = repo_namespace
        # Specifies whether the item is selected. Valid values:
        # - **0**: No.
        # - **1**: Yes.
        self.selected = selected
        # The dimension of the defense switch configuration. Valid values:
        # - **image_repo**: image repository ID.
        # 
        # This parameter is required.
        self.target_type = target_type
        # The type of the defense switch. Valid values:
        # - **image_repo**: image repository defense.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.selected is not None:
            result['Selected'] = self.selected

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

