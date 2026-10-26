# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListTemplatesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned data.
        self.current_page = current_page
        # The list of records returned for the current query.
        self.items = items
        # The number of records per page for the current query.
        self.page_size = page_size
        # The request ID, which can be used to trace the current API call.
        self.request_id = request_id
        # The total number of records that match the current query conditions.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListTemplatesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTemplatesResponseBodyItems(DaraModel):
    def __init__(
        self,
        current_risk_level: int = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        max_category_level: int = None,
        max_risk_level: int = None,
        name: str = None,
        status: int = None,
        support_edit: int = None,
        type: int = None,
    ):
        # The current sensitivity level of the template.
        self.current_risk_level = current_risk_level
        # The description of the classification and grading template.
        self.description = description
        # The creation time of the template. The value is a UNIX timestamp in milliseconds since 1970-01-01 00:00:00 UTC.
        self.gmt_create = gmt_create
        # The last modification time of the template. The value is a UNIX timestamp in milliseconds since 1970-01-01 00:00:00 UTC.
        self.gmt_modified = gmt_modified
        # The identifier of the classification and grading template.
        self.id = id
        # The maximum classification level supported by the template.
        self.max_category_level = max_category_level
        # The highest sensitivity level supported by the template.
        self.max_risk_level = max_risk_level
        # The name of the classification and grading template.
        self.name = name
        # The status of the template. Valid values: 0: Disabled. 1: Enabled primary template. 2: Active template. 3: General detection model.
        self.status = status
        # Specifies whether the template can be edited. Valid values: 0: Not supported. 1: Supported.
        self.support_edit = support_edit
        # The category of the template. Valid values: 1: Alibaba Cloud template. 2: Finance template. 3: Energy template. 4: Personal information security template. 5: Travel template. 65: General template. 66: Custom template. 67: Template from other cloud services.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_risk_level is not None:
            result['CurrentRiskLevel'] = self.current_risk_level

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.max_category_level is not None:
            result['MaxCategoryLevel'] = self.max_category_level

        if self.max_risk_level is not None:
            result['MaxRiskLevel'] = self.max_risk_level

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.support_edit is not None:
            result['SupportEdit'] = self.support_edit

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentRiskLevel') is not None:
            self.current_risk_level = m.get('CurrentRiskLevel')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxCategoryLevel') is not None:
            self.max_category_level = m.get('MaxCategoryLevel')

        if m.get('MaxRiskLevel') is not None:
            self.max_risk_level = m.get('MaxRiskLevel')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportEdit') is not None:
            self.support_edit = m.get('SupportEdit')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

