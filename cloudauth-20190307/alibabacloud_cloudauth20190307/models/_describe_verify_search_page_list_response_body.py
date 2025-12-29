# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifySearchPageListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeVerifySearchPageListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Paged list data.
        self.items = items
        # Number of items per page.
        self.page_size = page_size
        # ID of this request.
        self.request_id = request_id
        # Total number of pages.
        self.total_count = total_count
        # Total number of pages.
        self.total_page = total_page

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVerifySearchPageListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeVerifySearchPageListResponseBodyItems(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        certify_id: str = None,
        ext_info: main_models.DescribeVerifySearchPageListResponseBodyItemsExtInfo = None,
        gmt_verify: str = None,
        model: str = None,
        outer_order_no: str = None,
        passed: str = None,
        product_code: str = None,
        root: int = None,
        scene_id: int = None,
        simulator: int = None,
        sub_code: str = None,
        user_id: str = None,
        virtual_video: int = None,
    ):
        # Desensitized ID number.
        self.cert_no = cert_no
        # Certification ID.
        self.certify_id = certify_id
        # Extended information.
        self.ext_info = ext_info
        # Verification time of this authentication.
        self.gmt_verify = gmt_verify
        # Liveness detection scheme.
        self.model = model
        # Unique identifier for the customer request.
        self.outer_order_no = outer_order_no
        # Whether the certification passed. Values:
        # - **T**: Passed.
        # - **F**: Not passed.
        self.passed = passed
        # Product code.
        self.product_code = product_code
        # Whether it is root (pass 1 if selected, otherwise do not pass; corresponds to identity label risk type).
        self.root = root
        # Scene ID.
        self.scene_id = scene_id
        # Whether it is a simulator (pass 1 if selected, otherwise do not pass; corresponds to device label risk type).
        self.simulator = simulator
        # System returned error code.
        self.sub_code = sub_code
        # User ID.
        self.user_id = user_id
        # Whether it is a virtual adaptation (pass 1 if selected, otherwise do not pass; corresponds to behavior label risk type).
        self.virtual_video = virtual_video

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()

        if self.gmt_verify is not None:
            result['GmtVerify'] = self.gmt_verify

        if self.model is not None:
            result['Model'] = self.model

        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no

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

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.virtual_video is not None:
            result['VirtualVideo'] = self.virtual_video

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('ExtInfo') is not None:
            temp_model = main_models.DescribeVerifySearchPageListResponseBodyItemsExtInfo()
            self.ext_info = temp_model.from_map(m.get('ExtInfo'))

        if m.get('GmtVerify') is not None:
            self.gmt_verify = m.get('GmtVerify')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')

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

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VirtualVideo') is not None:
            self.virtual_video = m.get('VirtualVideo')

        return self

class DescribeVerifySearchPageListResponseBodyItemsExtInfo(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        device_risk: str = None,
        face_attack: str = None,
        face_attack_score: float = None,
        face_occlusion: str = None,
        id_card_verify_score: float = None,
        oss_bucket_name: str = None,
        oss_id_face_object_name: str = None,
        oss_id_national_emblem_object_name: str = None,
        oss_object_name: str = None,
        quality_score: float = None,
        verify_score: float = None,
        asr_texts: List[str] = None,
        screen_video_object_names: List[str] = None,
        voice_object_names: List[str] = None,
    ):
        # Desensitized name.
        self.cert_name = cert_name
        # Face guard label.
        self.device_risk = device_risk
        # Whether it is a face attack:
        # - **T**: Yes
        # - **F**: No
        self.face_attack = face_attack
        # Face attack score, with a range of 0~1. A value closer to 1 indicates a higher likelihood of an attack.
        self.face_attack_score = face_attack_score
        # Whether the face is occluded, T if yes, F otherwise.
        self.face_occlusion = face_occlusion
        # Face-to-ID card comparison score.
        self.id_card_verify_score = id_card_verify_score
        # The OSS bucket for the photo.
        self.oss_bucket_name = oss_bucket_name
        # OCR ID card face file name.
        self.oss_id_face_object_name = oss_id_face_object_name
        # OCR ID card national emblem file name.
        self.oss_id_national_emblem_object_name = oss_id_national_emblem_object_name
        # The name of the stored object.
        self.oss_object_name = oss_object_name
        # Liveness face quality score.
        self.quality_score = quality_score
        # Face comparison score.
        self.verify_score = verify_score
        # List of ASR texts.
        self.asr_texts = asr_texts
        # List of OSS file names for screen recording files.
        self.screen_video_object_names = screen_video_object_names
        # List of OSS file names for audio files.
        self.voice_object_names = voice_object_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.device_risk is not None:
            result['DeviceRisk'] = self.device_risk

        if self.face_attack is not None:
            result['FaceAttack'] = self.face_attack

        if self.face_attack_score is not None:
            result['FaceAttackScore'] = self.face_attack_score

        if self.face_occlusion is not None:
            result['FaceOcclusion'] = self.face_occlusion

        if self.id_card_verify_score is not None:
            result['IdCardVerifyScore'] = self.id_card_verify_score

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_id_face_object_name is not None:
            result['OssIdFaceObjectName'] = self.oss_id_face_object_name

        if self.oss_id_national_emblem_object_name is not None:
            result['OssIdNationalEmblemObjectName'] = self.oss_id_national_emblem_object_name

        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name

        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score

        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score

        if self.asr_texts is not None:
            result['asrTexts'] = self.asr_texts

        if self.screen_video_object_names is not None:
            result['screenVideoObjectNames'] = self.screen_video_object_names

        if self.voice_object_names is not None:
            result['voiceObjectNames'] = self.voice_object_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('DeviceRisk') is not None:
            self.device_risk = m.get('DeviceRisk')

        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')

        if m.get('FaceAttackScore') is not None:
            self.face_attack_score = m.get('FaceAttackScore')

        if m.get('FaceOcclusion') is not None:
            self.face_occlusion = m.get('FaceOcclusion')

        if m.get('IdCardVerifyScore') is not None:
            self.id_card_verify_score = m.get('IdCardVerifyScore')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssIdFaceObjectName') is not None:
            self.oss_id_face_object_name = m.get('OssIdFaceObjectName')

        if m.get('OssIdNationalEmblemObjectName') is not None:
            self.oss_id_national_emblem_object_name = m.get('OssIdNationalEmblemObjectName')

        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')

        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')

        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')

        if m.get('asrTexts') is not None:
            self.asr_texts = m.get('asrTexts')

        if m.get('screenVideoObjectNames') is not None:
            self.screen_video_object_names = m.get('screenVideoObjectNames')

        if m.get('voiceObjectNames') is not None:
            self.voice_object_names = m.get('voiceObjectNames')

        return self

