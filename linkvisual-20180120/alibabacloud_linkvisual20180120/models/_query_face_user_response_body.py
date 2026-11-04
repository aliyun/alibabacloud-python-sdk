# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryFaceUserResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryFaceUserResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The response data.
        self.data = data
        # The error message.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the API call is successful.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
            temp_model = main_models.QueryFaceUserResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryFaceUserResponseBodyData(DaraModel):
    def __init__(
        self,
        custom_user_id: str = None,
        face_pic_list: List[main_models.QueryFaceUserResponseBodyDataFacePicList] = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        # The user ID in the caller\\"s system.
        self.custom_user_id = custom_user_id
        # The list of face photo information.
        self.face_pic_list = face_pic_list
        # The username.
        self.name = name
        # The user parameters.
        self.params = params
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.face_pic_list:
            for v1 in self.face_pic_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id

        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k1 in self.face_pic_list:
                result['FacePicList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')

        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k1 in m.get('FacePicList'):
                temp_model = main_models.QueryFaceUserResponseBodyDataFacePicList()
                self.face_pic_list.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryFaceUserResponseBodyDataFacePicList(DaraModel):
    def __init__(
        self,
        face_md_5: str = None,
        face_url: str = None,
        feature_dtolist: List[main_models.QueryFaceUserResponseBodyDataFacePicListFeatureDTOList] = None,
    ):
        # The MD5 hash of the photo.
        self.face_md_5 = face_md_5
        # The URL of the photo.
        self.face_url = face_url
        # The list of face feature values.
        self.feature_dtolist = feature_dtolist

    def validate(self):
        if self.feature_dtolist:
            for v1 in self.feature_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5

        if self.face_url is not None:
            result['FaceUrl'] = self.face_url

        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k1 in self.feature_dtolist:
                result['FeatureDTOList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')

        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')

        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k1 in m.get('FeatureDTOList'):
                temp_model = main_models.QueryFaceUserResponseBodyDataFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k1))

        return self

class QueryFaceUserResponseBodyDataFacePicListFeatureDTOList(DaraModel):
    def __init__(
        self,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        algorithm_version: str = None,
        error_code: str = None,
        error_message: str = None,
        face_md_5: str = None,
    ):
        # The name of the algorithm.
        self.algorithm_name = algorithm_name
        # The provider of the algorithm.
        self.algorithm_provider = algorithm_provider
        # The version of the algorithm.
        self.algorithm_version = algorithm_version
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The MD5 hash of the face.
        self.face_md_5 = face_md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name

        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider

        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')

        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')

        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')

        return self

