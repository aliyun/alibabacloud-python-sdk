# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTrailStatusResponseBody(DaraModel):
    def __init__(
        self,
        is_logging: bool = None,
        latest_delivery_error: str = None,
        latest_delivery_log_service_error: str = None,
        latest_delivery_log_service_time: str = None,
        latest_delivery_time: str = None,
        oss_bucket_status: bool = None,
        request_id: str = None,
        sls_log_store_status: bool = None,
        start_logging_time: str = None,
        stop_logging_time: str = None,
    ):
        # Indicates whether logging is enabled for the trail. Valid values:
        # 
        # - true
        # 
        # - false
        self.is_logging = is_logging
        # The log of the last failed delivery.
        self.latest_delivery_error = latest_delivery_error
        # The log of the last failed delivery to Log Service.
        self.latest_delivery_log_service_error = latest_delivery_log_service_error
        # The most recent time when an event was delivered to Log Service.
        self.latest_delivery_log_service_time = latest_delivery_log_service_time
        # The most recent time when an event was delivered by the trail.
        self.latest_delivery_time = latest_delivery_time
        # Indicates whether the destination Object Storage Service (OSS) bucket is available. Valid values:
        # 
        # - true
        # 
        # - false
        self.oss_bucket_status = oss_bucket_status
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the destination Log Service Logstore is available. Valid values:
        # 
        # - true
        # 
        # - false
        self.sls_log_store_status = sls_log_store_status
        # The time when logging was last enabled for the trail.
        self.start_logging_time = start_logging_time
        # The time when logging was last disabled for the trail.
        self.stop_logging_time = stop_logging_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_logging is not None:
            result['IsLogging'] = self.is_logging

        if self.latest_delivery_error is not None:
            result['LatestDeliveryError'] = self.latest_delivery_error

        if self.latest_delivery_log_service_error is not None:
            result['LatestDeliveryLogServiceError'] = self.latest_delivery_log_service_error

        if self.latest_delivery_log_service_time is not None:
            result['LatestDeliveryLogServiceTime'] = self.latest_delivery_log_service_time

        if self.latest_delivery_time is not None:
            result['LatestDeliveryTime'] = self.latest_delivery_time

        if self.oss_bucket_status is not None:
            result['OssBucketStatus'] = self.oss_bucket_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_log_store_status is not None:
            result['SlsLogStoreStatus'] = self.sls_log_store_status

        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time

        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsLogging') is not None:
            self.is_logging = m.get('IsLogging')

        if m.get('LatestDeliveryError') is not None:
            self.latest_delivery_error = m.get('LatestDeliveryError')

        if m.get('LatestDeliveryLogServiceError') is not None:
            self.latest_delivery_log_service_error = m.get('LatestDeliveryLogServiceError')

        if m.get('LatestDeliveryLogServiceTime') is not None:
            self.latest_delivery_log_service_time = m.get('LatestDeliveryLogServiceTime')

        if m.get('LatestDeliveryTime') is not None:
            self.latest_delivery_time = m.get('LatestDeliveryTime')

        if m.get('OssBucketStatus') is not None:
            self.oss_bucket_status = m.get('OssBucketStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsLogStoreStatus') is not None:
            self.sls_log_store_status = m.get('SlsLogStoreStatus')

        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')

        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')

        return self

