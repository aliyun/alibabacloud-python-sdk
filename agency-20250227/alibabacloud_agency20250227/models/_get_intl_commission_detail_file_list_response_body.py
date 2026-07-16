# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20250227 import models as main_models
from darabonba.model import DaraModel

class GetIntlCommissionDetailFileListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIntlCommissionDetailFileListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data.
        self.data = data
        # The message information.
        self.message = message
        # RequestId
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetIntlCommissionDetailFileListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetIntlCommissionDetailFileListResponseBodyData(DaraModel):
    def __init__(
        self,
        bill_month: str = None,
        file_list: List[main_models.GetIntlCommissionDetailFileListResponseBodyDataFileList] = None,
        partner_uid: str = None,
    ):
        # The billing month.
        self.bill_month = bill_month
        # The file list object.
        self.file_list = file_list
        # The UID of the partner.
        self.partner_uid = partner_uid

    def validate(self):
        if self.file_list:
            for v1 in self.file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_month is not None:
            result['BillMonth'] = self.bill_month

        result['FileList'] = []
        if self.file_list is not None:
            for k1 in self.file_list:
                result['FileList'].append(k1.to_map() if k1 else None)

        if self.partner_uid is not None:
            result['PartnerUid'] = self.partner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillMonth') is not None:
            self.bill_month = m.get('BillMonth')

        self.file_list = []
        if m.get('FileList') is not None:
            for k1 in m.get('FileList'):
                temp_model = main_models.GetIntlCommissionDetailFileListResponseBodyDataFileList()
                self.file_list.append(temp_model.from_map(k1))

        if m.get('PartnerUid') is not None:
            self.partner_uid = m.get('PartnerUid')

        return self

class GetIntlCommissionDetailFileListResponseBodyDataFileList(DaraModel):
    def __init__(
        self,
        bucket_sync_status: str = None,
        commission_policy_name: str = None,
        file_name: str = None,
    ):
        # The push status of the OSS file. Valid values:
        # - 初始化状态: initialization status
        # - 处理中: processing
        # - 处理成功: processing succeeded
        # - 处理失败: processing failed.
        self.bucket_sync_status = bucket_sync_status
        # The commission policy name.
        self.commission_policy_name = commission_policy_name
        # The file name.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_sync_status is not None:
            result['BucketSyncStatus'] = self.bucket_sync_status

        if self.commission_policy_name is not None:
            result['CommissionPolicyName'] = self.commission_policy_name

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketSyncStatus') is not None:
            self.bucket_sync_status = m.get('BucketSyncStatus')

        if m.get('CommissionPolicyName') is not None:
            self.commission_policy_name = m.get('CommissionPolicyName')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

