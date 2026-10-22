# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitPenetrationTestRequest(DaraModel):
    def __init__(
        self,
        asset_list: str = None,
        is_thirdparty_test: bool = None,
        test_content: str = None,
        test_end_date: str = None,
        test_source_ips: str = None,
        test_start_date: str = None,
        test_steps: str = None,
        thirdparty_email: str = None,
        thirdparty_mobile: str = None,
        thirdparty_tester: str = None,
    ):
        # The asset list.
        # 
        # > The array supports a maximum of 50 IP addresses.
        self.asset_list = asset_list
        # Specifies whether the test is performed by a third-party testing service provider. Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        self.is_thirdparty_test = is_thirdparty_test
        # The test content.
        # 
        # > The content must not exceed 500 characters. Provide detailed information to facilitate the approval process.
        self.test_content = test_content
        # The end time of the test.
        self.test_end_date = test_end_date
        # The source IP addresses used for the test.
        # 
        # > A maximum of 50 IP addresses are supported. Separate multiple IP addresses with line breaks or commas (,). 0.0.0.0 indicates that all IP addresses are allowed. CIDR blocks such as 140.168.0.0/16 are not supported.
        self.test_source_ips = test_source_ips
        # The start date of the test.
        self.test_start_date = test_start_date
        # The test steps.
        # 
        # > The steps must not exceed 500 characters. Provide detailed information to facilitate the approval process.
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
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list

        if self.is_thirdparty_test is not None:
            result['IsThirdpartyTest'] = self.is_thirdparty_test

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
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')

        if m.get('IsThirdpartyTest') is not None:
            self.is_thirdparty_test = m.get('IsThirdpartyTest')

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

