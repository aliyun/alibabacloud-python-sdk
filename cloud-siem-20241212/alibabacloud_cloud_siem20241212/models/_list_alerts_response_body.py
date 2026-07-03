# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListAlertsResponseBody(DaraModel):
    def __init__(
        self,
        alerts: List[main_models.ListAlertsResponseBodyAlerts] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The alert details.
        self.alerts = alerts
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

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
        alert_record: str = None,
        alert_uuid: str = None,
    ):
        # The alert details.
        self.alert_record = alert_record
        # The alert UUID.
        self.alert_uuid = alert_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_record is not None:
            result['AlertRecord'] = self.alert_record

        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRecord') is not None:
            self.alert_record = m.get('AlertRecord')

        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        return self

