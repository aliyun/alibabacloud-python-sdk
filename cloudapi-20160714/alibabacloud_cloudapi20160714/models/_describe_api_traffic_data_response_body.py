# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiTrafficDataResponseBody(DaraModel):
    def __init__(
        self,
        call_downloads: main_models.DescribeApiTrafficDataResponseBodyCallDownloads = None,
        call_uploads: main_models.DescribeApiTrafficDataResponseBodyCallUploads = None,
        request_id: str = None,
    ):
        # The returned downlink traffic data of API calls. It is an array consisting of MonitorItem data.
        self.call_downloads = call_downloads
        # The returned uplink traffic data of API calls. It is an array consisting of MonitorItem data.
        self.call_uploads = call_uploads
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.call_downloads:
            self.call_downloads.validate()
        if self.call_uploads:
            self.call_uploads.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_downloads is not None:
            result['CallDownloads'] = self.call_downloads.to_map()

        if self.call_uploads is not None:
            result['CallUploads'] = self.call_uploads.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallDownloads') is not None:
            temp_model = main_models.DescribeApiTrafficDataResponseBodyCallDownloads()
            self.call_downloads = temp_model.from_map(m.get('CallDownloads'))

        if m.get('CallUploads') is not None:
            temp_model = main_models.DescribeApiTrafficDataResponseBodyCallUploads()
            self.call_uploads = temp_model.from_map(m.get('CallUploads'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApiTrafficDataResponseBodyCallUploads(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeApiTrafficDataResponseBodyCallUploadsMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for v1 in self.monitor_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k1 in self.monitor_item:
                result['MonitorItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k1 in m.get('MonitorItem'):
                temp_model = main_models.DescribeApiTrafficDataResponseBodyCallUploadsMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeApiTrafficDataResponseBodyCallUploadsMonitorItem(DaraModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        # The time of the monitoring metric. The time format follows the ISO 8601 standard and UTC time is used. Format: YYYY-MM-DDThh:mm:ssZ
        self.item_time = item_time
        # The value corresponding to the monitoring metric.
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_time is not None:
            result['ItemTime'] = self.item_time

        if self.item_value is not None:
            result['ItemValue'] = self.item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')

        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')

        return self

class DescribeApiTrafficDataResponseBodyCallDownloads(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeApiTrafficDataResponseBodyCallDownloadsMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for v1 in self.monitor_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k1 in self.monitor_item:
                result['MonitorItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k1 in m.get('MonitorItem'):
                temp_model = main_models.DescribeApiTrafficDataResponseBodyCallDownloadsMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeApiTrafficDataResponseBodyCallDownloadsMonitorItem(DaraModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        # The time of the monitoring metric. The time format follows the ISO 8601 standard and UTC time is used. Format: YYYY-MM-DDThh:mm:ssZ
        self.item_time = item_time
        # The value corresponding to the monitoring metric.
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_time is not None:
            result['ItemTime'] = self.item_time

        if self.item_value is not None:
            result['ItemValue'] = self.item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')

        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')

        return self

