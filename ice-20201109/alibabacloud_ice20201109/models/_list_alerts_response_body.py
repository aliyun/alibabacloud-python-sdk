# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListAlertsResponseBody(DaraModel):
    def __init__(
        self,
        alerts: List[main_models.ListAlertsResponseBodyAlerts] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The alerts.
        self.alerts = alerts
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Valid values: 1 to 100.
        self.page_size = page_size
        # **Request ID**
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.alerts:
            for v1 in self.alerts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alerts'] = []
        if self.alerts is not None:
            for k1 in self.alerts:
                result['Alerts'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alerts = []
        if m.get('Alerts') is not None:
            for k1 in m.get('Alerts'):
                temp_model = main_models.ListAlertsResponseBodyAlerts()
                self.alerts.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAlertsResponseBodyAlerts(DaraModel):
    def __init__(
        self,
        category: str = None,
        code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message: str = None,
        related_resource_arns: str = None,
        resource_arn: str = None,
    ):
        # The alert type.
        self.category = category
        # The error code.
        self.code = code
        # The time when the alert was received in UTC.
        self.gmt_create = gmt_create
        # The time when the alert was modified in UTC.
        self.gmt_modified = gmt_modified
        # The error message.
        self.message = message
        # The ARN of the related resource.
        self.related_resource_arns = related_resource_arns
        # The ARN of the resource.
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.code is not None:
            result['Code'] = self.code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message is not None:
            result['Message'] = self.message

        if self.related_resource_arns is not None:
            result['RelatedResourceArns'] = self.related_resource_arns

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RelatedResourceArns') is not None:
            self.related_resource_arns = m.get('RelatedResourceArns')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        return self

