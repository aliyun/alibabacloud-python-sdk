# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class AddUserSourceLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AddUserSourceLogConfigResponseBodyData = None,
        request_id: str = None,
    ):
        # The return value of the request.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.AddUserSourceLogConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddUserSourceLogConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        diplay_line: str = None,
        displayed: bool = None,
        imported: bool = None,
        main_user_id: int = None,
        source_log_code: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        # The detailed information about the SLS log.
        self.diplay_line = diplay_line
        # Indicates whether the details of the log collection task are returned. Valid values:
        self.displayed = displayed
        # Indicates whether the log is collected. Valid values:
        self.imported = imported
        # The ID of the Alibaba Cloud account that is used to purchase Threat Analysis.
        self.main_user_id = main_user_id
        # The code of the log.
        self.source_log_code = source_log_code
        # The code of the product.
        self.source_prod_code = source_prod_code
        # The ID of the Alibaba Cloud account for which the logs are collected.
        self.sub_user_id = sub_user_id
        # The name of the Alibaba Cloud account for which the logs are collected.
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diplay_line is not None:
            result['DiplayLine'] = self.diplay_line

        if self.displayed is not None:
            result['Displayed'] = self.displayed

        if self.imported is not None:
            result['Imported'] = self.imported

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code

        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiplayLine') is not None:
            self.diplay_line = m.get('DiplayLine')

        if m.get('Displayed') is not None:
            self.displayed = m.get('Displayed')

        if m.get('Imported') is not None:
            self.imported = m.get('Imported')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')

        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')

        return self

