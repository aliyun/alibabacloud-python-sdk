# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVerifyStatisticsResponseBodyResultObject = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Statistical results
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeVerifyStatisticsResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeVerifyStatisticsResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        init_device: int = None,
        init_device_id: int = None,
        init_device_id_success: int = None,
        init_device_success: int = None,
        init_service: int = None,
        init_service_id: int = None,
        init_service_id_success: int = None,
        init_service_success: int = None,
        items: List[main_models.DescribeVerifyStatisticsResponseBodyResultObjectItems] = None,
        verify_device: int = None,
        verify_device_id: int = None,
        verify_device_id_success: int = None,
        verify_device_id_success_passed: int = None,
        verify_device_success: int = None,
        verify_device_success_passed: int = None,
    ):
        # Number of client initializations.
        self.init_device = init_device
        # Number of identity deduplication client initializations.
        self.init_device_id = init_device_id
        # Number of successful identity deduplication client initializations.
        self.init_device_id_success = init_device_id_success
        # Number of client initialization calls.
        self.init_device_success = init_device_success
        # Number of service-side initializations.
        self.init_service = init_service
        # Total number of identity deduplication server initialization requests.
        self.init_service_id = init_service_id
        # Number of successful identity deduplication server initializations.
        self.init_service_id_success = init_service_id_success
        # Number of successful service-side initialization authentications.
        self.init_service_success = init_service_success
        # Daily pass/conversion rate (PV).
        self.items = items
        # Number of client verifications.
        self.verify_device = verify_device
        # Number of identity deduplication client authentications.
        self.verify_device_id = verify_device_id
        # Number of successful identity deduplication client verifications.
        self.verify_device_id_success = verify_device_id_success
        # Number of successful identity deduplication client authentications.
        self.verify_device_id_success_passed = verify_device_id_success_passed
        # Number of successful client authentications.
        self.verify_device_success = verify_device_success
        # Number of successful client authentications.
        self.verify_device_success_passed = verify_device_success_passed

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
        if self.init_device is not None:
            result['InitDevice'] = self.init_device

        if self.init_device_id is not None:
            result['InitDeviceId'] = self.init_device_id

        if self.init_device_id_success is not None:
            result['InitDeviceIdSuccess'] = self.init_device_id_success

        if self.init_device_success is not None:
            result['InitDeviceSuccess'] = self.init_device_success

        if self.init_service is not None:
            result['InitService'] = self.init_service

        if self.init_service_id is not None:
            result['InitServiceId'] = self.init_service_id

        if self.init_service_id_success is not None:
            result['InitServiceIdSuccess'] = self.init_service_id_success

        if self.init_service_success is not None:
            result['InitServiceSuccess'] = self.init_service_success

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.verify_device is not None:
            result['VerifyDevice'] = self.verify_device

        if self.verify_device_id is not None:
            result['VerifyDeviceId'] = self.verify_device_id

        if self.verify_device_id_success is not None:
            result['VerifyDeviceIdSuccess'] = self.verify_device_id_success

        if self.verify_device_id_success_passed is not None:
            result['VerifyDeviceIdSuccessPassed'] = self.verify_device_id_success_passed

        if self.verify_device_success is not None:
            result['VerifyDeviceSuccess'] = self.verify_device_success

        if self.verify_device_success_passed is not None:
            result['VerifyDeviceSuccessPassed'] = self.verify_device_success_passed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitDevice') is not None:
            self.init_device = m.get('InitDevice')

        if m.get('InitDeviceId') is not None:
            self.init_device_id = m.get('InitDeviceId')

        if m.get('InitDeviceIdSuccess') is not None:
            self.init_device_id_success = m.get('InitDeviceIdSuccess')

        if m.get('InitDeviceSuccess') is not None:
            self.init_device_success = m.get('InitDeviceSuccess')

        if m.get('InitService') is not None:
            self.init_service = m.get('InitService')

        if m.get('InitServiceId') is not None:
            self.init_service_id = m.get('InitServiceId')

        if m.get('InitServiceIdSuccess') is not None:
            self.init_service_id_success = m.get('InitServiceIdSuccess')

        if m.get('InitServiceSuccess') is not None:
            self.init_service_success = m.get('InitServiceSuccess')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVerifyStatisticsResponseBodyResultObjectItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('VerifyDevice') is not None:
            self.verify_device = m.get('VerifyDevice')

        if m.get('VerifyDeviceId') is not None:
            self.verify_device_id = m.get('VerifyDeviceId')

        if m.get('VerifyDeviceIdSuccess') is not None:
            self.verify_device_id_success = m.get('VerifyDeviceIdSuccess')

        if m.get('VerifyDeviceIdSuccessPassed') is not None:
            self.verify_device_id_success_passed = m.get('VerifyDeviceIdSuccessPassed')

        if m.get('VerifyDeviceSuccess') is not None:
            self.verify_device_success = m.get('VerifyDeviceSuccess')

        if m.get('VerifyDeviceSuccessPassed') is not None:
            self.verify_device_success_passed = m.get('VerifyDeviceSuccessPassed')

        return self

class DescribeVerifyStatisticsResponseBodyResultObjectItems(DaraModel):
    def __init__(
        self,
        date: str = None,
        init_device_pass_rate: str = None,
        init_service: int = None,
        init_service_conversion_rate: str = None,
        init_service_pass_rate: str = None,
        pass_rate: str = None,
    ):
        # Date.
        self.date = date
        # Client initialization pass rate.
        self.init_device_pass_rate = init_device_pass_rate
        # Number of server initializations.
        self.init_service = init_service
        # Server initialization conversion rate.
        self.init_service_conversion_rate = init_service_conversion_rate
        # Server initialization pass rate.
        self.init_service_pass_rate = init_service_pass_rate
        # Pass rate.
        self.pass_rate = pass_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.init_device_pass_rate is not None:
            result['InitDevicePassRate'] = self.init_device_pass_rate

        if self.init_service is not None:
            result['InitService'] = self.init_service

        if self.init_service_conversion_rate is not None:
            result['InitServiceConversionRate'] = self.init_service_conversion_rate

        if self.init_service_pass_rate is not None:
            result['InitServicePassRate'] = self.init_service_pass_rate

        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('InitDevicePassRate') is not None:
            self.init_device_pass_rate = m.get('InitDevicePassRate')

        if m.get('InitService') is not None:
            self.init_service = m.get('InitService')

        if m.get('InitServiceConversionRate') is not None:
            self.init_service_conversion_rate = m.get('InitServiceConversionRate')

        if m.get('InitServicePassRate') is not None:
            self.init_service_pass_rate = m.get('InitServicePassRate')

        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')

        return self

