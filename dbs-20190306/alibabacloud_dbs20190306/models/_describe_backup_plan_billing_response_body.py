# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPlanBillingResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        item: main_models.DescribeBackupPlanBillingResponseBodyItem = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The billing information of the backup plan.
        self.item = item
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.item is not None:
            result['Item'] = self.item.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Item') is not None:
            temp_model = main_models.DescribeBackupPlanBillingResponseBodyItem()
            self.item = temp_model.from_map(m.get('Item'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeBackupPlanBillingResponseBodyItem(DaraModel):
    def __init__(
        self,
        buy_charge_type: str = None,
        buy_create_timestamp: int = None,
        buy_expired_timestamp: int = None,
        buy_spec: str = None,
        cont_storage_size: int = None,
        full_storage_size: int = None,
        is_expired: bool = None,
        is_free_bytes_unlimited: bool = None,
        paied_bytes: int = None,
        quota_end_timestamp: int = None,
        quota_start_timestamp: int = None,
        total_free_bytes: int = None,
        used_full_bytes: int = None,
        used_increment_bytes: int = None,
    ):
        # The billing method of the instance. Valid values:
        # 
        # - **PREPAY**: subscription
        # 
        # - **POSTPAY**: pay-as-you-go
        self.buy_charge_type = buy_charge_type
        # The timestamp that indicates when the instance was purchased.
        self.buy_create_timestamp = buy_create_timestamp
        # The timestamp that indicates when the instance expires.
        # 
        # > This parameter is returned only when BuyChargeType is set to PREPAY.
        self.buy_expired_timestamp = buy_expired_timestamp
        # The instance type.
        self.buy_spec = buy_spec
        # The storage space used by incremental backup data. Unit: bytes.
        self.cont_storage_size = cont_storage_size
        # The storage space used by full backup data. Unit: bytes.
        self.full_storage_size = full_storage_size
        # Indicates whether the instance has expired.
        # 
        # > This parameter is returned only when BuyChargeType is set to PREPAY.
        self.is_expired = is_expired
        # Indicates whether the instance provides unlimited free backup traffic.
        self.is_free_bytes_unlimited = is_free_bytes_unlimited
        # The total paid backup traffic in the current month. Unit: bytes.
        self.paied_bytes = paied_bytes
        # The timestamp that indicates the end of the billing cycle for the free backup traffic.
        self.quota_end_timestamp = quota_end_timestamp
        # The timestamp that indicates the start of the billing cycle for the free backup traffic.
        self.quota_start_timestamp = quota_start_timestamp
        # The total free backup traffic in the current month. Unit: bytes.
        # 
        # > This parameter is returned only when BuyChargeType is set to PREPAY and IsFreeBytesUnlimited is false.
        self.total_free_bytes = total_free_bytes
        # The paid traffic for full backups in the current month. Unit: bytes.
        self.used_full_bytes = used_full_bytes
        # The paid traffic for incremental backups in the current month. Unit: bytes.
        self.used_increment_bytes = used_increment_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_charge_type is not None:
            result['BuyChargeType'] = self.buy_charge_type

        if self.buy_create_timestamp is not None:
            result['BuyCreateTimestamp'] = self.buy_create_timestamp

        if self.buy_expired_timestamp is not None:
            result['BuyExpiredTimestamp'] = self.buy_expired_timestamp

        if self.buy_spec is not None:
            result['BuySpec'] = self.buy_spec

        if self.cont_storage_size is not None:
            result['ContStorageSize'] = self.cont_storage_size

        if self.full_storage_size is not None:
            result['FullStorageSize'] = self.full_storage_size

        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired

        if self.is_free_bytes_unlimited is not None:
            result['IsFreeBytesUnlimited'] = self.is_free_bytes_unlimited

        if self.paied_bytes is not None:
            result['PaiedBytes'] = self.paied_bytes

        if self.quota_end_timestamp is not None:
            result['QuotaEndTimestamp'] = self.quota_end_timestamp

        if self.quota_start_timestamp is not None:
            result['QuotaStartTimestamp'] = self.quota_start_timestamp

        if self.total_free_bytes is not None:
            result['TotalFreeBytes'] = self.total_free_bytes

        if self.used_full_bytes is not None:
            result['UsedFullBytes'] = self.used_full_bytes

        if self.used_increment_bytes is not None:
            result['UsedIncrementBytes'] = self.used_increment_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyChargeType') is not None:
            self.buy_charge_type = m.get('BuyChargeType')

        if m.get('BuyCreateTimestamp') is not None:
            self.buy_create_timestamp = m.get('BuyCreateTimestamp')

        if m.get('BuyExpiredTimestamp') is not None:
            self.buy_expired_timestamp = m.get('BuyExpiredTimestamp')

        if m.get('BuySpec') is not None:
            self.buy_spec = m.get('BuySpec')

        if m.get('ContStorageSize') is not None:
            self.cont_storage_size = m.get('ContStorageSize')

        if m.get('FullStorageSize') is not None:
            self.full_storage_size = m.get('FullStorageSize')

        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')

        if m.get('IsFreeBytesUnlimited') is not None:
            self.is_free_bytes_unlimited = m.get('IsFreeBytesUnlimited')

        if m.get('PaiedBytes') is not None:
            self.paied_bytes = m.get('PaiedBytes')

        if m.get('QuotaEndTimestamp') is not None:
            self.quota_end_timestamp = m.get('QuotaEndTimestamp')

        if m.get('QuotaStartTimestamp') is not None:
            self.quota_start_timestamp = m.get('QuotaStartTimestamp')

        if m.get('TotalFreeBytes') is not None:
            self.total_free_bytes = m.get('TotalFreeBytes')

        if m.get('UsedFullBytes') is not None:
            self.used_full_bytes = m.get('UsedFullBytes')

        if m.get('UsedIncrementBytes') is not None:
            self.used_increment_bytes = m.get('UsedIncrementBytes')

        return self

