# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifySearchPageListRequest(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        current_page: str = None,
        end_date: str = None,
        has_device_risk: bool = None,
        model: str = None,
        outer_order_no: str = None,
        page_size: str = None,
        passed: str = None,
        product_code: str = None,
        root: int = None,
        scene_id: str = None,
        simulator: int = None,
        start_date: str = None,
        sub_code: str = None,
        sub_codes: str = None,
        virtual_video: int = None,
    ):
        # ID number.
        self.cert_no = cert_no
        # Authentication ID.
        self.certify_id = certify_id
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # End date of the query. The format is a Unix timestamp, in milliseconds.
        self.end_date = end_date
        # Whether there is device risk (pass true if root = 1 or simulator = 1 or virtual_video = 1).
        self.has_device_risk = has_device_risk
        # Liveness detection model.
        self.model = model
        # Unique identifier for the customer request.
        self.outer_order_no = outer_order_no
        # Number of items per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Whether the authentication passed:
        # - **T**: Passed
        # - **F**: Not passed
        self.passed = passed
        # Product code.
        self.product_code = product_code
        # Whether it is rooted (pass 1 if selected, otherwise do not pass; corresponds to identity label risk type).
        self.root = root
        # Scene ID.
        self.scene_id = scene_id
        # Whether it is a simulator (pass 1 if selected, otherwise do not pass; corresponds to device label risk type).
        self.simulator = simulator
        # Start date of the query.
        self.start_date = start_date
        # Result Code. For detailed values, please refer to: [SubCode Explanation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/error-code-person-verify?spm=a2c4g.11186623.0.0.6015566ebArcFw#d88910e172fgg).
        self.sub_code = sub_code
        # Comma-separated Result Codes. For detailed values, please refer to: [SubCode Explanation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/error-code-person-verify?spm=a2c4g.11186623.0.0.6015566ebArcFw#d88910e172fgg).
        self.sub_codes = sub_codes
        # Whether it is a virtual adaptation (pass 1 if selected, otherwise do not pass; corresponds to behavior label risk type).
        self.virtual_video = virtual_video

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.has_device_risk is not None:
            result['HasDeviceRisk'] = self.has_device_risk

        if self.model is not None:
            result['Model'] = self.model

        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.root is not None:
            result['Root'] = self.root

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.simulator is not None:
            result['Simulator'] = self.simulator

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.sub_codes is not None:
            result['SubCodes'] = self.sub_codes

        if self.virtual_video is not None:
            result['VirtualVideo'] = self.virtual_video

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('HasDeviceRisk') is not None:
            self.has_device_risk = m.get('HasDeviceRisk')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Root') is not None:
            self.root = m.get('Root')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Simulator') is not None:
            self.simulator = m.get('Simulator')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('SubCodes') is not None:
            self.sub_codes = m.get('SubCodes')

        if m.get('VirtualVideo') is not None:
            self.virtual_video = m.get('VirtualVideo')

        return self

