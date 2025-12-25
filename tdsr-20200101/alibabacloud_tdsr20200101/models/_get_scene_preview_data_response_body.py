# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tdsr20200101 import models as main_models
from darabonba.model import DaraModel

class GetScenePreviewDataResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.GetScenePreviewDataResponseBodyAccessDeniedDetail = None,
        code: int = None,
        data: main_models.GetScenePreviewDataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

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
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.GetScenePreviewDataResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetScenePreviewDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetScenePreviewDataResponseBodyData(DaraModel):
    def __init__(
        self,
        model: main_models.GetScenePreviewDataResponseBodyDataModel = None,
        tags: List[main_models.GetScenePreviewDataResponseBodyDataTags] = None,
    ):
        self.model = model
        self.tags = tags

    def validate(self):
        if self.model:
            self.model.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['Model'] = self.model.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            temp_model = main_models.GetScenePreviewDataResponseBodyDataModel()
            self.model = temp_model.from_map(m.get('Model'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetScenePreviewDataResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetScenePreviewDataResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        config: main_models.GetScenePreviewDataResponseBodyDataTagsConfig = None,
        id: str = None,
        position: List[float] = None,
        position_pano_cube: List[float] = None,
        type: str = None,
    ):
        self.config = config
        self.id = id
        self.position = position
        self.position_pano_cube = position_pano_cube
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.position is not None:
            result['Position'] = self.position

        if self.position_pano_cube is not None:
            result['PositionPanoCube'] = self.position_pano_cube

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.GetScenePreviewDataResponseBodyDataTagsConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('PositionPanoCube') is not None:
            self.position_pano_cube = m.get('PositionPanoCube')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetScenePreviewDataResponseBodyDataTagsConfig(DaraModel):
    def __init__(
        self,
        background_color: str = None,
        button_config: main_models.GetScenePreviewDataResponseBodyDataTagsConfigButtonConfig = None,
        content: str = None,
        form_img_size: List[int] = None,
        form_jump_type: bool = None,
        form_select_img_type: str = None,
        images: List[str] = None,
        is_tag_visible_by_3d: bool = None,
        link: str = None,
        pano_id: str = None,
        position: List[float] = None,
        position_pano_cube: List[float] = None,
        related_pano_ids: List[str] = None,
        scene_id: int = None,
        title: str = None,
        video: str = None,
    ):
        self.background_color = background_color
        self.button_config = button_config
        self.content = content
        self.form_img_size = form_img_size
        self.form_jump_type = form_jump_type
        self.form_select_img_type = form_select_img_type
        self.images = images
        self.is_tag_visible_by_3d = is_tag_visible_by_3d
        self.link = link
        self.pano_id = pano_id
        self.position = position
        self.position_pano_cube = position_pano_cube
        self.related_pano_ids = related_pano_ids
        self.scene_id = scene_id
        self.title = title
        self.video = video

    def validate(self):
        if self.button_config:
            self.button_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color

        if self.button_config is not None:
            result['ButtonConfig'] = self.button_config.to_map()

        if self.content is not None:
            result['Content'] = self.content

        if self.form_img_size is not None:
            result['FormImgSize'] = self.form_img_size

        if self.form_jump_type is not None:
            result['FormJumpType'] = self.form_jump_type

        if self.form_select_img_type is not None:
            result['FormSelectImgType'] = self.form_select_img_type

        if self.images is not None:
            result['Images'] = self.images

        if self.is_tag_visible_by_3d is not None:
            result['IsTagVisibleBy3d'] = self.is_tag_visible_by_3d

        if self.link is not None:
            result['Link'] = self.link

        if self.pano_id is not None:
            result['PanoId'] = self.pano_id

        if self.position is not None:
            result['Position'] = self.position

        if self.position_pano_cube is not None:
            result['PositionPanoCube'] = self.position_pano_cube

        if self.related_pano_ids is not None:
            result['RelatedPanoIds'] = self.related_pano_ids

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.title is not None:
            result['Title'] = self.title

        if self.video is not None:
            result['Video'] = self.video

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')

        if m.get('ButtonConfig') is not None:
            temp_model = main_models.GetScenePreviewDataResponseBodyDataTagsConfigButtonConfig()
            self.button_config = temp_model.from_map(m.get('ButtonConfig'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FormImgSize') is not None:
            self.form_img_size = m.get('FormImgSize')

        if m.get('FormJumpType') is not None:
            self.form_jump_type = m.get('FormJumpType')

        if m.get('FormSelectImgType') is not None:
            self.form_select_img_type = m.get('FormSelectImgType')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('IsTagVisibleBy3d') is not None:
            self.is_tag_visible_by_3d = m.get('IsTagVisibleBy3d')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('PanoId') is not None:
            self.pano_id = m.get('PanoId')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('PositionPanoCube') is not None:
            self.position_pano_cube = m.get('PositionPanoCube')

        if m.get('RelatedPanoIds') is not None:
            self.related_pano_ids = m.get('RelatedPanoIds')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Video') is not None:
            self.video = m.get('Video')

        return self

class GetScenePreviewDataResponseBodyDataTagsConfigButtonConfig(DaraModel):
    def __init__(
        self,
        custom_text: str = None,
        type: str = None,
    ):
        self.custom_text = custom_text
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_text is not None:
            result['CustomText'] = self.custom_text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomText') is not None:
            self.custom_text = m.get('CustomText')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetScenePreviewDataResponseBodyDataModel(DaraModel):
    def __init__(
        self,
        model_path: str = None,
        pano_list: List[main_models.GetScenePreviewDataResponseBodyDataModelPanoList] = None,
        texture_model_path: str = None,
        texture_pano_path: str = None,
    ):
        self.model_path = model_path
        self.pano_list = pano_list
        self.texture_model_path = texture_model_path
        self.texture_pano_path = texture_pano_path

    def validate(self):
        if self.pano_list:
            for v1 in self.pano_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_path is not None:
            result['ModelPath'] = self.model_path

        result['PanoList'] = []
        if self.pano_list is not None:
            for k1 in self.pano_list:
                result['PanoList'].append(k1.to_map() if k1 else None)

        if self.texture_model_path is not None:
            result['TextureModelPath'] = self.texture_model_path

        if self.texture_pano_path is not None:
            result['TexturePanoPath'] = self.texture_pano_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')

        self.pano_list = []
        if m.get('PanoList') is not None:
            for k1 in m.get('PanoList'):
                temp_model = main_models.GetScenePreviewDataResponseBodyDataModelPanoList()
                self.pano_list.append(temp_model.from_map(k1))

        if m.get('TextureModelPath') is not None:
            self.texture_model_path = m.get('TextureModelPath')

        if m.get('TexturePanoPath') is not None:
            self.texture_pano_path = m.get('TexturePanoPath')

        return self

class GetScenePreviewDataResponseBodyDataModelPanoList(DaraModel):
    def __init__(
        self,
        cur_room_pic_list: List[str] = None,
        enabled: bool = None,
        floor_idx: str = None,
        id: str = None,
        main_image: bool = None,
        neighbours: List[str] = None,
        position: main_models.GetScenePreviewDataResponseBodyDataModelPanoListPosition = None,
        raw_name: str = None,
        resource: str = None,
        room_idx: str = None,
        sub_scene_id: str = None,
        token: str = None,
        virtual_id: str = None,
        virtual_name: str = None,
    ):
        self.cur_room_pic_list = cur_room_pic_list
        self.enabled = enabled
        self.floor_idx = floor_idx
        self.id = id
        self.main_image = main_image
        self.neighbours = neighbours
        self.position = position
        self.raw_name = raw_name
        self.resource = resource
        self.room_idx = room_idx
        self.sub_scene_id = sub_scene_id
        # token
        self.token = token
        self.virtual_id = virtual_id
        self.virtual_name = virtual_name

    def validate(self):
        if self.position:
            self.position.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_room_pic_list is not None:
            result['CurRoomPicList'] = self.cur_room_pic_list

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.floor_idx is not None:
            result['FloorIdx'] = self.floor_idx

        if self.id is not None:
            result['Id'] = self.id

        if self.main_image is not None:
            result['MainImage'] = self.main_image

        if self.neighbours is not None:
            result['Neighbours'] = self.neighbours

        if self.position is not None:
            result['Position'] = self.position.to_map()

        if self.raw_name is not None:
            result['RawName'] = self.raw_name

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.room_idx is not None:
            result['RoomIdx'] = self.room_idx

        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id

        if self.token is not None:
            result['Token'] = self.token

        if self.virtual_id is not None:
            result['VirtualId'] = self.virtual_id

        if self.virtual_name is not None:
            result['VirtualName'] = self.virtual_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurRoomPicList') is not None:
            self.cur_room_pic_list = m.get('CurRoomPicList')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FloorIdx') is not None:
            self.floor_idx = m.get('FloorIdx')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MainImage') is not None:
            self.main_image = m.get('MainImage')

        if m.get('Neighbours') is not None:
            self.neighbours = m.get('Neighbours')

        if m.get('Position') is not None:
            temp_model = main_models.GetScenePreviewDataResponseBodyDataModelPanoListPosition()
            self.position = temp_model.from_map(m.get('Position'))

        if m.get('RawName') is not None:
            self.raw_name = m.get('RawName')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('RoomIdx') is not None:
            self.room_idx = m.get('RoomIdx')

        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VirtualId') is not None:
            self.virtual_id = m.get('VirtualId')

        if m.get('VirtualName') is not None:
            self.virtual_name = m.get('VirtualName')

        return self

class GetScenePreviewDataResponseBodyDataModelPanoListPosition(DaraModel):
    def __init__(
        self,
        rotation: List[float] = None,
        spot: List[float] = None,
        viewpoint: List[float] = None,
    ):
        self.rotation = rotation
        self.spot = spot
        self.viewpoint = viewpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rotation is not None:
            result['Rotation'] = self.rotation

        if self.spot is not None:
            result['Spot'] = self.spot

        if self.viewpoint is not None:
            result['Viewpoint'] = self.viewpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rotation') is not None:
            self.rotation = m.get('Rotation')

        if m.get('Spot') is not None:
            self.spot = m.get('Spot')

        if m.get('Viewpoint') is not None:
            self.viewpoint = m.get('Viewpoint')

        return self

class GetScenePreviewDataResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

