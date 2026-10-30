# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class QueryPenetrationTestDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryPenetrationTestDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # - **200**: Success.
        # - **Other values (400 and 500)**: Failure.
        self.code = code
        # The response content.
        self.data = data
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # - **true**: The call is successful.                               
        # - **false**: The call fails.
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
            temp_model = main_models.QueryPenetrationTestDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPenetrationTestDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        apply_time: int = None,
        asset_type: str = None,
        id: int = None,
        ip: str = None,
        is_thirdparty_test: bool = None,
        status: str = None,
        test_content: str = None,
        test_end_date: int = None,
        test_source_ips: str = None,
        test_start_date: int = None,
        test_steps: str = None,
        thirdparty_email: str = None,
        thirdparty_mobile: str = None,
        thirdparty_tester: str = None,
    ):
        # The application time.
        self.apply_time = apply_time
        # The type of the asset. Valid values:
        # 
        # - **EIP**: public IP address in a VPC.
        # - **SLB**: load balancing.
        # - **ECS**: public IP address in the classic network.
        self.asset_type = asset_type
        # The unique identity of the application record.
        # 
        # > This field is of the Long type. Precision loss may occur during the procedure to serialize or deserialize the numeric sequence. Ensure that the value does not exceed 9007199254740991.
        self.id = id
        # IP
        self.ip = ip
        # Indicates whether the test is performed by a third-party service provider. Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        self.is_thirdparty_test = is_thirdparty_test
        # The task status. Valid values:
        # 
        # - **early_end**: The user applied for early termination.
        # - **expired**: The authorization has expired.
        # - **auditing**: Under review.
        # - **approved**: Approved.
        # - **rejected**: Rejected.
        self.status = status
        # The test content.
        # 
        # > - Maximum 500 characters. Provide detailed information to increase the chance of passing the review.
        self.test_content = test_content
        # The test end time.
        self.test_end_date = test_end_date
        # The source IP addresses used for the test.
        # 
        # > A maximum of 50 IP addresses are supported. Separate multiple IP addresses with line breaks or commas (,). Specify 0.0.0.0 to allow all IP addresses. CIDR blocks are not supported, such as 140.168.0.0/16.
        self.test_source_ips = test_source_ips
        # The test start date.
        self.test_start_date = test_start_date
        # The test steps.
        # 
        # > Maximum 500 characters. Provide detailed information to increase the chance of passing the review.
        self.test_steps = test_steps
        # The email address of the third-party tester.
        self.thirdparty_email = thirdparty_email
        # The mobile phone number of the third-party tester.
        self.thirdparty_mobile = thirdparty_mobile
        # The third-party tester.
        self.thirdparty_tester = thirdparty_tester

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.is_thirdparty_test is not None:
            result['IsThirdpartyTest'] = self.is_thirdparty_test

        if self.status is not None:
            result['Status'] = self.status

        if self.test_content is not None:
            result['TestContent'] = self.test_content

        if self.test_end_date is not None:
            result['TestEndDate'] = self.test_end_date

        if self.test_source_ips is not None:
            result['TestSourceIps'] = self.test_source_ips

        if self.test_start_date is not None:
            result['TestStartDate'] = self.test_start_date

        if self.test_steps is not None:
            result['TestSteps'] = self.test_steps

        if self.thirdparty_email is not None:
            result['ThirdpartyEmail'] = self.thirdparty_email

        if self.thirdparty_mobile is not None:
            result['ThirdpartyMobile'] = self.thirdparty_mobile

        if self.thirdparty_tester is not None:
            result['ThirdpartyTester'] = self.thirdparty_tester

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IsThirdpartyTest') is not None:
            self.is_thirdparty_test = m.get('IsThirdpartyTest')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TestContent') is not None:
            self.test_content = m.get('TestContent')

        if m.get('TestEndDate') is not None:
            self.test_end_date = m.get('TestEndDate')

        if m.get('TestSourceIps') is not None:
            self.test_source_ips = m.get('TestSourceIps')

        if m.get('TestStartDate') is not None:
            self.test_start_date = m.get('TestStartDate')

        if m.get('TestSteps') is not None:
            self.test_steps = m.get('TestSteps')

        if m.get('ThirdpartyEmail') is not None:
            self.thirdparty_email = m.get('ThirdpartyEmail')

        if m.get('ThirdpartyMobile') is not None:
            self.thirdparty_mobile = m.get('ThirdpartyMobile')

        if m.get('ThirdpartyTester') is not None:
            self.thirdparty_tester = m.get('ThirdpartyTester')

        return self

