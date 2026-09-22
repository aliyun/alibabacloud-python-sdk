# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListAiAppWarningByPageResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ext: main_models.ListAiAppWarningByPageResponseBodyExt = None,
        items: List[main_models.ListAiAppWarningByPageResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The extension field.
        self.ext = ext
        # The data on the current page.
        self.items = items
        # The number of entries per page.
        self.page_size = page_size
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.ext:
            self.ext.validate()
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

        if self.ext is not None:
            result['Ext'] = self.ext.to_map()

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

        if m.get('Ext') is not None:
            temp_model = main_models.ListAiAppWarningByPageResponseBodyExt()
            self.ext = temp_model.from_map(m.get('Ext'))

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListAiAppWarningByPageResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAiAppWarningByPageResponseBodyItems(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        labels: List[main_models.ListAiAppWarningByPageResponseBodyItemsLabels] = None,
        service_code: str = None,
        trace_id: str = None,
        warning_count: int = None,
        warning_time: str = None,
    ):
        # appId。
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The list of labels.
        self.labels = labels
        # The service code.
        self.service_code = service_code
        # The trace ID used to correlate and trace alert events.
        self.trace_id = trace_id
        # The number of alerts.
        self.warning_count = warning_count
        # The alert time in the format of YYYY-MM-DD HH:mm:ss.
        self.warning_time = warning_time

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count

        if self.warning_time is not None:
            result['WarningTime'] = self.warning_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListAiAppWarningByPageResponseBodyItemsLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')

        if m.get('WarningTime') is not None:
            self.warning_time = m.get('WarningTime')

        return self

class ListAiAppWarningByPageResponseBodyItemsLabels(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
        label_desc: str = None,
        type: str = None,
    ):
        # The count.
        self.count = count
        # The label name.
        self.label = label
        # The label description.
        self.label_desc = label_desc
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        if self.label_desc is not None:
            result['LabelDesc'] = self.label_desc

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelDesc') is not None:
            self.label_desc = m.get('LabelDesc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListAiAppWarningByPageResponseBodyExt(DaraModel):
    def __init__(
        self,
        option: Dict[str, Any] = None,
    ):
        # The option.
        self.option = option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option is not None:
            result['Option'] = self.option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            self.option = m.get('Option')

        return self

