# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListDataQualityTemplatesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # Paged query results of data quality rule templates.
        self.page_info = page_info
        # The API request ID, which is generated as a UUID.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListDataQualityTemplatesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityTemplatesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        data_quality_templates: List[main_models.ListDataQualityTemplatesResponseBodyPageInfoDataQualityTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of rule templates.
        self.data_quality_templates = data_quality_templates
        # The page number.
        self.page_number = page_number
        # The number of pages.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_templates:
            for v1 in self.data_quality_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityTemplates'] = []
        if self.data_quality_templates is not None:
            for k1 in self.data_quality_templates:
                result['DataQualityTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_templates = []
        if m.get('DataQualityTemplates') is not None:
            for k1 in m.get('DataQualityTemplates'):
                temp_model = main_models.ListDataQualityTemplatesResponseBodyPageInfoDataQualityTemplates()
                self.data_quality_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityTemplatesResponseBodyPageInfoDataQualityTemplates(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        id: str = None,
        modify_time: int = None,
        modify_user: str = None,
        owner: str = None,
        project_id: int = None,
        spec: str = None,
    ):
        # The time when the data quality rule template was created.
        self.create_time = create_time
        # The creator of the data quality rule template.
        self.create_user = create_user
        # The ID of the data quality rule template.
        self.id = id
        # The time when the data quality rule template was updated.
        self.modify_time = modify_time
        # The last updater of the data quality rule template.
        self.modify_user = modify_user
        # The owner of the data quality rule template.
        self.owner = owner
        # The project ID.
        self.project_id = project_id
        # Specific configurations of the data quality rule template. For more information, see [Data quality Spec configuration description](~2963394~).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

