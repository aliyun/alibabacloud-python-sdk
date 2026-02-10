# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAccountLabelResponseBody(DaraModel):
    def __init__(
        self,
        account_label_list: List[main_models.GetAccountLabelResponseBodyAccountLabelList] = None,
        request_id: str = None,
    ):
        # The tag list.
        self.account_label_list = account_label_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.account_label_list:
            for v1 in self.account_label_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountLabelList'] = []
        if self.account_label_list is not None:
            for k1 in self.account_label_list:
                result['AccountLabelList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_label_list = []
        if m.get('AccountLabelList') is not None:
            for k1 in m.get('AccountLabelList'):
                temp_model = main_models.GetAccountLabelResponseBodyAccountLabelList()
                self.account_label_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccountLabelResponseBodyAccountLabelList(DaraModel):
    def __init__(
        self,
        label_series: str = None,
        label_status: bool = None,
    ):
        # The tag information.
        self.label_series = label_series
        # Indicates whether the tag is valid.
        # 
        # *   **true**
        # *   **false**
        self.label_status = label_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_series is not None:
            result['LabelSeries'] = self.label_series

        if self.label_status is not None:
            result['LabelStatus'] = self.label_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelSeries') is not None:
            self.label_series = m.get('LabelSeries')

        if m.get('LabelStatus') is not None:
            self.label_status = m.get('LabelStatus')

        return self

