# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeListFaceVerifyInfosResponseBody(DaraModel):
    def __init__(
        self,
        face_verify_infos: List[main_models.DescribeListFaceVerifyInfosResponseBodyFaceVerifyInfos] = None,
        items_per_page: int = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
        total_pages: int = None,
    ):
        # The list of facial recognition authentication records.
        self.face_verify_infos = face_verify_infos
        # The specified page number returned.
        self.items_per_page = items_per_page
        # The current page number for pagination.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # The total number of authentication records.
        self.total_count = total_count
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.face_verify_infos:
            for v1 in self.face_verify_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FaceVerifyInfos'] = []
        if self.face_verify_infos is not None:
            for k1 in self.face_verify_infos:
                result['FaceVerifyInfos'].append(k1.to_map() if k1 else None)

        if self.items_per_page is not None:
            result['ItemsPerPage'] = self.items_per_page

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_verify_infos = []
        if m.get('FaceVerifyInfos') is not None:
            for k1 in m.get('FaceVerifyInfos'):
                temp_model = main_models.DescribeListFaceVerifyInfosResponseBodyFaceVerifyInfos()
                self.face_verify_infos.append(temp_model.from_map(k1))

        if m.get('ItemsPerPage') is not None:
            self.items_per_page = m.get('ItemsPerPage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeListFaceVerifyInfosResponseBodyFaceVerifyInfos(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        cert_name: str = None,
        cert_no: str = None,
        certify_id: str = None,
        create_time: str = None,
        scene_id: int = None,
        status: int = None,
    ):
        # The business code.
        self.biz_code = biz_code
        # The name.
        self.cert_name = cert_name
        # The certificate number.
        self.cert_no = cert_no
        # The certificate ID.
        self.certify_id = certify_id
        # The creation time of the facial recognition record.
        self.create_time = create_time
        # The scene ID.
        self.scene_id = scene_id
        # The authentication status. Valid values:
        # - **1**: Authentication passed.
        # - **2**: Authentication failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

