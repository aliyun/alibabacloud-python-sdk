# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AnchorResponse(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        anchor_material_name: str = None,
        anchor_type: str = None,
        cover_height: int = None,
        cover_rate: str = None,
        cover_thumbnail_url: str = None,
        cover_url: str = None,
        cover_weight: int = None,
        digital_human_type: str = None,
        gender: str = None,
        resource_type_desc: str = None,
        status: str = None,
        use_scene: str = None,
    ):
        self.anchor_id = anchor_id
        self.anchor_material_name = anchor_material_name
        self.anchor_type = anchor_type
        self.cover_height = cover_height
        self.cover_rate = cover_rate
        self.cover_thumbnail_url = cover_thumbnail_url
        self.cover_url = cover_url
        self.cover_weight = cover_weight
        self.digital_human_type = digital_human_type
        self.gender = gender
        self.resource_type_desc = resource_type_desc
        self.status = status
        self.use_scene = use_scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['anchorId'] = self.anchor_id
        if self.anchor_material_name is not None:
            result['anchorMaterialName'] = self.anchor_material_name
        if self.anchor_type is not None:
            result['anchorType'] = self.anchor_type
        if self.cover_height is not None:
            result['coverHeight'] = self.cover_height
        if self.cover_rate is not None:
            result['coverRate'] = self.cover_rate
        if self.cover_thumbnail_url is not None:
            result['coverThumbnailUrl'] = self.cover_thumbnail_url
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.cover_weight is not None:
            result['coverWeight'] = self.cover_weight
        if self.digital_human_type is not None:
            result['digitalHumanType'] = self.digital_human_type
        if self.gender is not None:
            result['gender'] = self.gender
        if self.resource_type_desc is not None:
            result['resourceTypeDesc'] = self.resource_type_desc
        if self.status is not None:
            result['status'] = self.status
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorId') is not None:
            self.anchor_id = m.get('anchorId')
        if m.get('anchorMaterialName') is not None:
            self.anchor_material_name = m.get('anchorMaterialName')
        if m.get('anchorType') is not None:
            self.anchor_type = m.get('anchorType')
        if m.get('coverHeight') is not None:
            self.cover_height = m.get('coverHeight')
        if m.get('coverRate') is not None:
            self.cover_rate = m.get('coverRate')
        if m.get('coverThumbnailUrl') is not None:
            self.cover_thumbnail_url = m.get('coverThumbnailUrl')
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('coverWeight') is not None:
            self.cover_weight = m.get('coverWeight')
        if m.get('digitalHumanType') is not None:
            self.digital_human_type = m.get('digitalHumanType')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('resourceTypeDesc') is not None:
            self.resource_type_desc = m.get('resourceTypeDesc')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        return self


class UploadInfo(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        policy_signature: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.access_id = access_id
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.policy = policy
        # This parameter is required.
        self.policy_signature = policy_signature
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['accessId'] = self.access_id
        if self.host is not None:
            result['host'] = self.host
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.policy_signature is not None:
            result['policySignature'] = self.policy_signature
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('policySignature') is not None:
            self.policy_signature = m.get('policySignature')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetOssUploadTokenResult(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upload_info: UploadInfo = None,
    ):
        self.request_id = request_id
        # This parameter is required.
        self.upload_info = upload_info

    def validate(self):
        if self.upload_info:
            self.upload_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.upload_info is not None:
            result['uploadInfo'] = self.upload_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('uploadInfo') is not None:
            temp_model = UploadInfo()
            self.upload_info = temp_model.from_map(m['uploadInfo'])
        return self


class Illustration(TeaModel):
    def __init__(
        self,
        illustration_id: int = None,
        oss: str = None,
    ):
        self.illustration_id = illustration_id
        self.oss = oss

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.illustration_id is not None:
            result['illustrationId'] = self.illustration_id
        if self.oss is not None:
            result['oss'] = self.oss
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('illustrationId') is not None:
            self.illustration_id = m.get('illustrationId')
        if m.get('oss') is not None:
            self.oss = m.get('oss')
        return self


class IllustrationResult(TeaModel):
    def __init__(
        self,
        illustration: Illustration = None,
        request_id: str = None,
    ):
        self.illustration = illustration
        self.request_id = request_id

    def validate(self):
        if self.illustration:
            self.illustration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.illustration is not None:
            result['illustration'] = self.illustration.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('illustration') is not None:
            temp_model = Illustration()
            self.illustration = temp_model.from_map(m['illustration'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class IllustrationTask(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        illustration_ids: List[int] = None,
        illustration_task_id: int = None,
        task_status: str = None,
        text_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.illustration_ids = illustration_ids
        self.illustration_task_id = illustration_task_id
        self.task_status = task_status
        self.text_id = text_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.illustration_ids is not None:
            result['illustrationIds'] = self.illustration_ids
        if self.illustration_task_id is not None:
            result['illustrationTaskId'] = self.illustration_task_id
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.text_id is not None:
            result['textId'] = self.text_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('illustrationIds') is not None:
            self.illustration_ids = m.get('illustrationIds')
        if m.get('illustrationTaskId') is not None:
            self.illustration_task_id = m.get('illustrationTaskId')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('textId') is not None:
            self.text_id = m.get('textId')
        return self


class IllustrationTaskCreateCmd(TeaModel):
    def __init__(
        self,
        background_type: int = None,
        dst_height: int = None,
        dst_width: int = None,
        idempotent_id: str = None,
        nums: int = None,
        oss_paths: List[str] = None,
        sticker_text: str = None,
    ):
        self.background_type = background_type
        self.dst_height = dst_height
        self.dst_width = dst_width
        self.idempotent_id = idempotent_id
        self.nums = nums
        self.oss_paths = oss_paths
        self.sticker_text = sticker_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_type is not None:
            result['backgroundType'] = self.background_type
        if self.dst_height is not None:
            result['dstHeight'] = self.dst_height
        if self.dst_width is not None:
            result['dstWidth'] = self.dst_width
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.nums is not None:
            result['nums'] = self.nums
        if self.oss_paths is not None:
            result['ossPaths'] = self.oss_paths
        if self.sticker_text is not None:
            result['stickerText'] = self.sticker_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backgroundType') is not None:
            self.background_type = m.get('backgroundType')
        if m.get('dstHeight') is not None:
            self.dst_height = m.get('dstHeight')
        if m.get('dstWidth') is not None:
            self.dst_width = m.get('dstWidth')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('nums') is not None:
            self.nums = m.get('nums')
        if m.get('ossPaths') is not None:
            self.oss_paths = m.get('ossPaths')
        if m.get('stickerText') is not None:
            self.sticker_text = m.get('stickerText')
        return self


class IllustrationTaskResult(TeaModel):
    def __init__(
        self,
        illustration_task: IllustrationTask = None,
        request_id: str = None,
    ):
        self.illustration_task = illustration_task
        self.request_id = request_id

    def validate(self):
        if self.illustration_task:
            self.illustration_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.illustration_task is not None:
            result['illustrationTask'] = self.illustration_task.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('illustrationTask') is not None:
            temp_model = IllustrationTask()
            self.illustration_task = temp_model.from_map(m['illustrationTask'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ReferenceTag(TeaModel):
    def __init__(
        self,
        reference_content: str = None,
        reference_title: str = None,
    ):
        self.reference_content = reference_content
        self.reference_title = reference_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference_content is not None:
            result['referenceContent'] = self.reference_content
        if self.reference_title is not None:
            result['referenceTitle'] = self.reference_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referenceContent') is not None:
            self.reference_content = m.get('referenceContent')
        if m.get('referenceTitle') is not None:
            self.reference_title = m.get('referenceTitle')
        return self


class Text(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        desc: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        illustration_task_id_list: List[int] = None,
        publish_status: str = None,
        text_content: str = None,
        text_id: int = None,
        text_illustration_tag: bool = None,
        text_mode_type: str = None,
        text_status: str = None,
        text_style_type: str = None,
        text_task_id: int = None,
        text_themes: List[str] = None,
        title: str = None,
        user_name_create: str = None,
        user_name_modified: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        # This parameter is required.
        self.desc = desc
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.illustration_task_id_list = illustration_task_id_list
        self.publish_status = publish_status
        self.text_content = text_content
        # This parameter is required.
        self.text_id = text_id
        self.text_illustration_tag = text_illustration_tag
        self.text_mode_type = text_mode_type
        # This parameter is required.
        self.text_status = text_status
        self.text_style_type = text_style_type
        # This parameter is required.
        self.text_task_id = text_task_id
        self.text_themes = text_themes
        self.title = title
        # This parameter is required.
        self.user_name_create = user_name_create
        # This parameter is required.
        self.user_name_modified = user_name_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.agent_name is not None:
            result['agentName'] = self.agent_name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.illustration_task_id_list is not None:
            result['illustrationTaskIdList'] = self.illustration_task_id_list
        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status
        if self.text_content is not None:
            result['textContent'] = self.text_content
        if self.text_id is not None:
            result['textId'] = self.text_id
        if self.text_illustration_tag is not None:
            result['textIllustrationTag'] = self.text_illustration_tag
        if self.text_mode_type is not None:
            result['textModeType'] = self.text_mode_type
        if self.text_status is not None:
            result['textStatus'] = self.text_status
        if self.text_style_type is not None:
            result['textStyleType'] = self.text_style_type
        if self.text_task_id is not None:
            result['textTaskId'] = self.text_task_id
        if self.text_themes is not None:
            result['textThemes'] = self.text_themes
        if self.title is not None:
            result['title'] = self.title
        if self.user_name_create is not None:
            result['userNameCreate'] = self.user_name_create
        if self.user_name_modified is not None:
            result['userNameModified'] = self.user_name_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('illustrationTaskIdList') is not None:
            self.illustration_task_id_list = m.get('illustrationTaskIdList')
        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')
        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')
        if m.get('textId') is not None:
            self.text_id = m.get('textId')
        if m.get('textIllustrationTag') is not None:
            self.text_illustration_tag = m.get('textIllustrationTag')
        if m.get('textModeType') is not None:
            self.text_mode_type = m.get('textModeType')
        if m.get('textStatus') is not None:
            self.text_status = m.get('textStatus')
        if m.get('textStyleType') is not None:
            self.text_style_type = m.get('textStyleType')
        if m.get('textTaskId') is not None:
            self.text_task_id = m.get('textTaskId')
        if m.get('textThemes') is not None:
            self.text_themes = m.get('textThemes')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userNameCreate') is not None:
            self.user_name_create = m.get('userNameCreate')
        if m.get('userNameModified') is not None:
            self.user_name_modified = m.get('userNameModified')
        return self


class TextQueryResult(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        texts: List[Text] = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.texts = texts
        self.total = total

    def validate(self):
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['texts'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.texts = []
        if m.get('texts') is not None:
            for k in m.get('texts'):
                temp_model = Text()
                self.texts.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class TextResult(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        text: Text = None,
    ):
        self.request_id = request_id
        # This parameter is required.
        self.text = text

    def validate(self):
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.text is not None:
            result['text'] = self.text.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('text') is not None:
            temp_model = Text()
            self.text = temp_model.from_map(m['text'])
        return self


class TextTask(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        content_requirement: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        introduction: str = None,
        nums: int = None,
        point: str = None,
        reference_tag: ReferenceTag = None,
        related_rag_id: int = None,
        style: str = None,
        target: str = None,
        text_ids: List[int] = None,
        text_mode_type: str = None,
        text_task_id: int = None,
        text_task_status: str = None,
        texts: List[Text] = None,
        theme: str = None,
        theme_desc: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.content_requirement = content_requirement
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.introduction = introduction
        # This parameter is required.
        self.nums = nums
        self.point = point
        self.reference_tag = reference_tag
        self.related_rag_id = related_rag_id
        # This parameter is required.
        self.style = style
        self.target = target
        self.text_ids = text_ids
        # This parameter is required.
        self.text_mode_type = text_mode_type
        self.text_task_id = text_task_id
        self.text_task_status = text_task_status
        self.texts = texts
        self.theme = theme
        self.theme_desc = theme_desc

    def validate(self):
        if self.reference_tag:
            self.reference_tag.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.agent_name is not None:
            result['agentName'] = self.agent_name
        if self.content_requirement is not None:
            result['contentRequirement'] = self.content_requirement
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.introduction is not None:
            result['introduction'] = self.introduction
        if self.nums is not None:
            result['nums'] = self.nums
        if self.point is not None:
            result['point'] = self.point
        if self.reference_tag is not None:
            result['referenceTag'] = self.reference_tag.to_map()
        if self.related_rag_id is not None:
            result['relatedRagId'] = self.related_rag_id
        if self.style is not None:
            result['style'] = self.style
        if self.target is not None:
            result['target'] = self.target
        if self.text_ids is not None:
            result['textIds'] = self.text_ids
        if self.text_mode_type is not None:
            result['textModeType'] = self.text_mode_type
        if self.text_task_id is not None:
            result['textTaskId'] = self.text_task_id
        if self.text_task_status is not None:
            result['textTaskStatus'] = self.text_task_status
        result['texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['texts'].append(k.to_map() if k else None)
        if self.theme is not None:
            result['theme'] = self.theme
        if self.theme_desc is not None:
            result['themeDesc'] = self.theme_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')
        if m.get('contentRequirement') is not None:
            self.content_requirement = m.get('contentRequirement')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('introduction') is not None:
            self.introduction = m.get('introduction')
        if m.get('nums') is not None:
            self.nums = m.get('nums')
        if m.get('point') is not None:
            self.point = m.get('point')
        if m.get('referenceTag') is not None:
            temp_model = ReferenceTag()
            self.reference_tag = temp_model.from_map(m['referenceTag'])
        if m.get('relatedRagId') is not None:
            self.related_rag_id = m.get('relatedRagId')
        if m.get('style') is not None:
            self.style = m.get('style')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('textIds') is not None:
            self.text_ids = m.get('textIds')
        if m.get('textModeType') is not None:
            self.text_mode_type = m.get('textModeType')
        if m.get('textTaskId') is not None:
            self.text_task_id = m.get('textTaskId')
        if m.get('textTaskStatus') is not None:
            self.text_task_status = m.get('textTaskStatus')
        self.texts = []
        if m.get('texts') is not None:
            for k in m.get('texts'):
                temp_model = Text()
                self.texts.append(temp_model.from_map(k))
        if m.get('theme') is not None:
            self.theme = m.get('theme')
        if m.get('themeDesc') is not None:
            self.theme_desc = m.get('themeDesc')
        return self


class TextTaskCreateCmd(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        content_requirement: str = None,
        idempotent_id: str = None,
        industry: str = None,
        introduction: str = None,
        number: int = None,
        point: str = None,
        reference_tag: ReferenceTag = None,
        related_rag_ids: List[int] = None,
        style: str = None,
        target: str = None,
        text_mode_type: str = None,
        theme: str = None,
        themes: List[str] = None,
    ):
        self.agent_id = agent_id
        self.content_requirement = content_requirement
        self.idempotent_id = idempotent_id
        self.industry = industry
        self.introduction = introduction
        # This parameter is required.
        self.number = number
        self.point = point
        self.reference_tag = reference_tag
        self.related_rag_ids = related_rag_ids
        # This parameter is required.
        self.style = style
        self.target = target
        # This parameter is required.
        self.text_mode_type = text_mode_type
        self.theme = theme
        self.themes = themes

    def validate(self):
        if self.reference_tag:
            self.reference_tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.content_requirement is not None:
            result['contentRequirement'] = self.content_requirement
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.industry is not None:
            result['industry'] = self.industry
        if self.introduction is not None:
            result['introduction'] = self.introduction
        if self.number is not None:
            result['number'] = self.number
        if self.point is not None:
            result['point'] = self.point
        if self.reference_tag is not None:
            result['referenceTag'] = self.reference_tag.to_map()
        if self.related_rag_ids is not None:
            result['relatedRagIds'] = self.related_rag_ids
        if self.style is not None:
            result['style'] = self.style
        if self.target is not None:
            result['target'] = self.target
        if self.text_mode_type is not None:
            result['textModeType'] = self.text_mode_type
        if self.theme is not None:
            result['theme'] = self.theme
        if self.themes is not None:
            result['themes'] = self.themes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('contentRequirement') is not None:
            self.content_requirement = m.get('contentRequirement')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('introduction') is not None:
            self.introduction = m.get('introduction')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('point') is not None:
            self.point = m.get('point')
        if m.get('referenceTag') is not None:
            temp_model = ReferenceTag()
            self.reference_tag = temp_model.from_map(m['referenceTag'])
        if m.get('relatedRagIds') is not None:
            self.related_rag_ids = m.get('relatedRagIds')
        if m.get('style') is not None:
            self.style = m.get('style')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('textModeType') is not None:
            self.text_mode_type = m.get('textModeType')
        if m.get('theme') is not None:
            self.theme = m.get('theme')
        if m.get('themes') is not None:
            self.themes = m.get('themes')
        return self


class TextTaskResult(TeaModel):
    def __init__(
        self,
        text_task: TextTask = None,
    ):
        self.text_task = text_task

    def validate(self):
        if self.text_task:
            self.text_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text_task is not None:
            result['textTask'] = self.text_task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('textTask') is not None:
            temp_model = TextTask()
            self.text_task = temp_model.from_map(m['textTask'])
        return self


class TextTheme(TeaModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
    ):
        self.desc = desc
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TextThemeListResult(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        text_theme_list: List[TextTheme] = None,
    ):
        self.request_id = request_id
        # This parameter is required.
        self.text_theme_list = text_theme_list

    def validate(self):
        if self.text_theme_list:
            for k in self.text_theme_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['textThemeList'] = []
        if self.text_theme_list is not None:
            for k in self.text_theme_list:
                result['textThemeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.text_theme_list = []
        if m.get('textThemeList') is not None:
            for k in m.get('textThemeList'):
                temp_model = TextTheme()
                self.text_theme_list.append(temp_model.from_map(k))
        return self


class VoiceModelResponse(TeaModel):
    def __init__(
        self,
        resource_type_desc: str = None,
        use_scene: str = None,
        voice_desc: str = None,
        voice_gender: str = None,
        voice_id: int = None,
        voice_language: str = None,
        voice_model: str = None,
        voice_name: str = None,
        voice_type: str = None,
        voice_url: str = None,
    ):
        self.resource_type_desc = resource_type_desc
        self.use_scene = use_scene
        self.voice_desc = voice_desc
        self.voice_gender = voice_gender
        self.voice_id = voice_id
        self.voice_language = voice_language
        self.voice_model = voice_model
        self.voice_name = voice_name
        self.voice_type = voice_type
        self.voice_url = voice_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type_desc is not None:
            result['resourceTypeDesc'] = self.resource_type_desc
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        if self.voice_desc is not None:
            result['voiceDesc'] = self.voice_desc
        if self.voice_gender is not None:
            result['voiceGender'] = self.voice_gender
        if self.voice_id is not None:
            result['voiceId'] = self.voice_id
        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language
        if self.voice_model is not None:
            result['voiceModel'] = self.voice_model
        if self.voice_name is not None:
            result['voiceName'] = self.voice_name
        if self.voice_type is not None:
            result['voiceType'] = self.voice_type
        if self.voice_url is not None:
            result['voiceUrl'] = self.voice_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceTypeDesc') is not None:
            self.resource_type_desc = m.get('resourceTypeDesc')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        if m.get('voiceDesc') is not None:
            self.voice_desc = m.get('voiceDesc')
        if m.get('voiceGender') is not None:
            self.voice_gender = m.get('voiceGender')
        if m.get('voiceId') is not None:
            self.voice_id = m.get('voiceId')
        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')
        if m.get('voiceModel') is not None:
            self.voice_model = m.get('voiceModel')
        if m.get('voiceName') is not None:
            self.voice_name = m.get('voiceName')
        if m.get('voiceType') is not None:
            self.voice_type = m.get('voiceType')
        if m.get('voiceUrl') is not None:
            self.voice_url = m.get('voiceUrl')
        return self


class AddTextFeedbackRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        quality: int = None,
        text_id: int = None,
    ):
        self.content = content
        self.quality = quality
        self.text_id = text_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.quality is not None:
            result['quality'] = self.quality
        if self.text_id is not None:
            result['textId'] = self.text_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('quality') is not None:
            self.quality = m.get('quality')
        if m.get('textId') is not None:
            self.text_id = m.get('textId')
        return self


class AddTextFeedbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddTextFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddTextFeedbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddTextFeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSessionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        session_id: str = None,
    ):
        self.project_id = project_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CheckSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CheckSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CountTextRequest(TeaModel):
    def __init__(
        self,
        generation_source: str = None,
        industry: str = None,
        publish_status: str = None,
        style: str = None,
    ):
        # API
        self.generation_source = generation_source
        self.industry = industry
        self.publish_status = publish_status
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation_source is not None:
            result['generationSource'] = self.generation_source
        if self.industry is not None:
            result['industry'] = self.industry
        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status
        if self.style is not None:
            result['style'] = self.style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationSource') is not None:
            self.generation_source = m.get('generationSource')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')
        if m.get('style') is not None:
            self.style = m.get('style')
        return self


class CountTextResponseBodyCountTextCmdList(TeaModel):
    def __init__(
        self,
        count: int = None,
        theme: str = None,
    ):
        self.count = count
        self.theme = theme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.theme is not None:
            result['theme'] = self.theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('theme') is not None:
            self.theme = m.get('theme')
        return self


class CountTextResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        count_text_cmd_list: List[CountTextResponseBodyCountTextCmdList] = None,
    ):
        self.request_id = request_id
        self.count_text_cmd_list = count_text_cmd_list

    def validate(self):
        if self.count_text_cmd_list:
            for k in self.count_text_cmd_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['countTextCmdList'] = []
        if self.count_text_cmd_list is not None:
            for k in self.count_text_cmd_list:
                result['countTextCmdList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.count_text_cmd_list = []
        if m.get('countTextCmdList') is not None:
            for k in m.get('countTextCmdList'):
                temp_model = CountTextResponseBodyCountTextCmdList()
                self.count_text_cmd_list.append(temp_model.from_map(k))
        return self


class CountTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CountTextResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CountTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIllustrationTaskRequest(TeaModel):
    def __init__(
        self,
        body: IllustrationTaskCreateCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = IllustrationTaskCreateCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIllustrationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IllustrationTaskResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IllustrationTaskResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTextTaskRequest(TeaModel):
    def __init__(
        self,
        body: TextTaskCreateCmd = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TextTaskCreateCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTextTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextTaskResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TextTaskResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIllustrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IllustrationResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IllustrationResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIllustrationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IllustrationTaskResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IllustrationTaskResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssUploadTokenRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_type: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        return self


class GetOssUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOssUploadTokenResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOssUploadTokenResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectTaskRequest(TeaModel):
    def __init__(
        self,
        idempotent_id: str = None,
        task_id: str = None,
    ):
        self.idempotent_id = idempotent_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        status: str = None,
        video_download_url: str = None,
        video_duration: int = None,
        video_url: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.status = status
        self.video_download_url = video_download_url
        self.video_duration = video_duration
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        if self.video_download_url is not None:
            result['videoDownloadUrl'] = self.video_download_url
        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('videoDownloadUrl') is not None:
            self.video_download_url = m.get('videoDownloadUrl')
        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class GetProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TextResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTextTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextTaskResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TextTaskResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTextTemplateRequest(TeaModel):
    def __init__(
        self,
        industry: str = None,
    ):
        self.industry = industry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry is not None:
            result['industry'] = self.industry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        return self


class GetTextTemplateResponseBodyAvailableIndustryTextModeTypesTextStyles(TeaModel):
    def __init__(
        self,
        desc: str = None,
        disabled: bool = None,
        name: str = None,
        template_key: str = None,
    ):
        self.desc = desc
        self.disabled = disabled
        self.name = name
        self.template_key = template_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.name is not None:
            result['name'] = self.name
        if self.template_key is not None:
            result['templateKey'] = self.template_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('templateKey') is not None:
            self.template_key = m.get('templateKey')
        return self


class GetTextTemplateResponseBodyAvailableIndustryTextModeTypes(TeaModel):
    def __init__(
        self,
        name: str = None,
        text_styles: List[GetTextTemplateResponseBodyAvailableIndustryTextModeTypesTextStyles] = None,
    ):
        self.name = name
        self.text_styles = text_styles

    def validate(self):
        if self.text_styles:
            for k in self.text_styles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        result['textStyles'] = []
        if self.text_styles is not None:
            for k in self.text_styles:
                result['textStyles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        self.text_styles = []
        if m.get('textStyles') is not None:
            for k in m.get('textStyles'):
                temp_model = GetTextTemplateResponseBodyAvailableIndustryTextModeTypesTextStyles()
                self.text_styles.append(temp_model.from_map(k))
        return self


class GetTextTemplateResponseBodyAvailableIndustry(TeaModel):
    def __init__(
        self,
        name: str = None,
        text_mode_types: List[GetTextTemplateResponseBodyAvailableIndustryTextModeTypes] = None,
    ):
        self.name = name
        self.text_mode_types = text_mode_types

    def validate(self):
        if self.text_mode_types:
            for k in self.text_mode_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        result['textModeTypes'] = []
        if self.text_mode_types is not None:
            for k in self.text_mode_types:
                result['textModeTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        self.text_mode_types = []
        if m.get('textModeTypes') is not None:
            for k in m.get('textModeTypes'):
                temp_model = GetTextTemplateResponseBodyAvailableIndustryTextModeTypes()
                self.text_mode_types.append(temp_model.from_map(k))
        return self


class GetTextTemplateResponseBody(TeaModel):
    def __init__(
        self,
        available_industry: GetTextTemplateResponseBodyAvailableIndustry = None,
        request_id: str = None,
    ):
        self.available_industry = available_industry
        self.request_id = request_id

    def validate(self):
        if self.available_industry:
            self.available_industry.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_industry is not None:
            result['availableIndustry'] = self.available_industry.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableIndustry') is not None:
            temp_model = GetTextTemplateResponseBodyAvailableIndustry()
            self.available_industry = temp_model.from_map(m['availableIndustry'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTextTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTextTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTextTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnchorRequest(TeaModel):
    def __init__(
        self,
        anchor_type: str = None,
        cover_rate: str = None,
        digital_human_type: str = None,
        page_number: int = None,
        page_size: int = None,
        use_scene: str = None,
    ):
        self.anchor_type = anchor_type
        self.cover_rate = cover_rate
        self.digital_human_type = digital_human_type
        self.page_number = page_number
        self.page_size = page_size
        self.use_scene = use_scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_type is not None:
            result['anchorType'] = self.anchor_type
        if self.cover_rate is not None:
            result['coverRate'] = self.cover_rate
        if self.digital_human_type is not None:
            result['digitalHumanType'] = self.digital_human_type
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorType') is not None:
            self.anchor_type = m.get('anchorType')
        if m.get('coverRate') is not None:
            self.cover_rate = m.get('coverRate')
        if m.get('digitalHumanType') is not None:
            self.digital_human_type = m.get('digitalHumanType')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        return self


class ListAnchorResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        error_message: str = None,
        list: List[AnchorResponse] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # code
        self.code = code
        self.error_code = error_code
        self.error_message = error_message
        self.list = list
        # requestId
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = AnchorResponse()
                self.list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAnchorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnchorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAnchorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextThemesRequest(TeaModel):
    def __init__(
        self,
        industry: str = None,
    ):
        self.industry = industry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry is not None:
            result['industry'] = self.industry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        return self


class ListTextThemesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextThemeListResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TextThemeListResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTextsRequest(TeaModel):
    def __init__(
        self,
        generation_source: str = None,
        industry: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        publish_status: str = None,
        text_style_type: str = None,
        text_theme: str = None,
    ):
        self.generation_source = generation_source
        self.industry = industry
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.publish_status = publish_status
        self.text_style_type = text_style_type
        self.text_theme = text_theme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation_source is not None:
            result['generationSource'] = self.generation_source
        if self.industry is not None:
            result['industry'] = self.industry
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status
        if self.text_style_type is not None:
            result['textStyleType'] = self.text_style_type
        if self.text_theme is not None:
            result['textTheme'] = self.text_theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationSource') is not None:
            self.generation_source = m.get('generationSource')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')
        if m.get('textStyleType') is not None:
            self.text_style_type = m.get('textStyleType')
        if m.get('textTheme') is not None:
            self.text_theme = m.get('textTheme')
        return self


class ListTextsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextQueryResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TextQueryResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVoiceModelsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        use_scene: str = None,
        voice_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.use_scene = use_scene
        self.voice_type = voice_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        if self.voice_type is not None:
            result['voiceType'] = self.voice_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        if m.get('voiceType') is not None:
            self.voice_type = m.get('voiceType')
        return self


class ListVoiceModelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        error_message: str = None,
        list: List[VoiceModelResponse] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.error_code = error_code
        self.error_message = error_message
        self.list = list
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = VoiceModelResponse()
                self.list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListVoiceModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVoiceModelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVoiceModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvatarProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class QueryAvatarProjectResponseBody(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        error_msg: str = None,
        project_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.agent_id = agent_id
        self.error_msg = error_msg
        self.project_name = project_name
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryAvatarProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAvatarProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvatarResourceRequest(TeaModel):
    def __init__(
        self,
        idempotent_id: str = None,
    ):
        self.idempotent_id = idempotent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        return self


class QueryAvatarResourceResponseBodyQueryResourceInfoList(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        type: str = None,
        valid_period_time: str = None,
    ):
        self.resource_id = resource_id
        self.type = type
        self.valid_period_time = valid_period_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.type is not None:
            result['type'] = self.type
        if self.valid_period_time is not None:
            result['validPeriodTime'] = self.valid_period_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('validPeriodTime') is not None:
            self.valid_period_time = m.get('validPeriodTime')
        return self


class QueryAvatarResourceResponseBody(TeaModel):
    def __init__(
        self,
        query_resource_info_list: List[QueryAvatarResourceResponseBodyQueryResourceInfoList] = None,
        request_id: str = None,
    ):
        self.query_resource_info_list = query_resource_info_list
        self.request_id = request_id

    def validate(self):
        if self.query_resource_info_list:
            for k in self.query_resource_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['queryResourceInfoList'] = []
        if self.query_resource_info_list is not None:
            for k in self.query_resource_info_list:
                result['queryResourceInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_resource_info_list = []
        if m.get('queryResourceInfoList') is not None:
            for k in m.get('queryResourceInfoList'):
                temp_model = QueryAvatarResourceResponseBodyQueryResourceInfoList()
                self.query_resource_info_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryAvatarResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAvatarResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAvatarResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectResourceRequest(TeaModel):
    def __init__(
        self,
        idempotent_id: str = None,
    ):
        self.idempotent_id = idempotent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        return self


class SelectResourceResponseBodyResourceInfoList(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        last_expire: int = None,
        remain_count: int = None,
        resource_type: int = None,
        unit: str = None,
    ):
        self.expire_time = expire_time
        self.last_expire = last_expire
        self.remain_count = remain_count
        self.resource_type = resource_type
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.last_expire is not None:
            result['lastExpire'] = self.last_expire
        if self.remain_count is not None:
            result['remainCount'] = self.remain_count
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('lastExpire') is not None:
            self.last_expire = m.get('lastExpire')
        if m.get('remainCount') is not None:
            self.remain_count = m.get('remainCount')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class SelectResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_info_list: List[SelectResourceResponseBodyResourceInfoList] = None,
    ):
        self.request_id = request_id
        self.resource_info_list = resource_info_list

    def validate(self):
        if self.resource_info_list:
            for k in self.resource_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceInfoList'] = []
        if self.resource_info_list is not None:
            for k in self.resource_info_list:
                result['resourceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resource_info_list = []
        if m.get('resourceInfoList') is not None:
            for k in m.get('resourceInfoList'):
                temp_model = SelectResourceResponseBodyResourceInfoList()
                self.resource_info_list.append(temp_model.from_map(k))
        return self


class SelectResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SelectResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTextMsgRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        request_id: str = None,
        session_id: str = None,
        text: str = None,
        type: int = None,
    ):
        self.project_id = project_id
        self.request_id = request_id
        self.session_id = session_id
        self.text = text
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.text is not None:
            result['text'] = self.text
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SendTextMsgResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SendTextMsgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendTextMsgResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendTextMsgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAvatarSessionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        request_id: str = None,
    ):
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartAvatarSessionResponseBody(TeaModel):
    def __init__(
        self,
        channel_token: str = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.channel_token = channel_token
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_token is not None:
            result['channelToken'] = self.channel_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToken') is not None:
            self.channel_token = m.get('channelToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class StartAvatarSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAvatarSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartAvatarSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAvatarSessionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        session_id: str = None,
    ):
        self.project_id = project_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class StopAvatarSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class StopAvatarSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAvatarSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopAvatarSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopProjectTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class StopProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopProjectTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitProjectTaskRequestFramesLayersMaterial(TeaModel):
    def __init__(
        self,
        format: str = None,
        id: str = None,
        url: str = None,
    ):
        self.format = format
        self.id = id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['format'] = self.format
        if self.id is not None:
            result['id'] = self.id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class SubmitProjectTaskRequestFramesLayers(TeaModel):
    def __init__(
        self,
        height: int = None,
        index: int = None,
        material: SubmitProjectTaskRequestFramesLayersMaterial = None,
        position_x: int = None,
        position_y: int = None,
        type: str = None,
        width: int = None,
    ):
        self.height = height
        self.index = index
        self.material = material
        self.position_x = position_x
        self.position_y = position_y
        self.type = type
        self.width = width

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.index is not None:
            result['index'] = self.index
        if self.material is not None:
            result['material'] = self.material.to_map()
        if self.position_x is not None:
            result['positionX'] = self.position_x
        if self.position_y is not None:
            result['positionY'] = self.position_y
        if self.type is not None:
            result['type'] = self.type
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('material') is not None:
            temp_model = SubmitProjectTaskRequestFramesLayersMaterial()
            self.material = temp_model.from_map(m['material'])
        if m.get('positionX') is not None:
            self.position_x = m.get('positionX')
        if m.get('positionY') is not None:
            self.position_y = m.get('positionY')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class SubmitProjectTaskRequestFramesSubtitle(TeaModel):
    def __init__(
        self,
        alignment: str = None,
        background_color: str = None,
        font: str = None,
        font_color: str = None,
        font_size: int = None,
        max_char_length: int = None,
        position_x: int = None,
        position_y: int = None,
        text_height: int = None,
        text_width: int = None,
    ):
        self.alignment = alignment
        self.background_color = background_color
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.max_char_length = max_char_length
        self.position_x = position_x
        self.position_y = position_y
        self.text_height = text_height
        self.text_width = text_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alignment is not None:
            result['alignment'] = self.alignment
        if self.background_color is not None:
            result['backgroundColor'] = self.background_color
        if self.font is not None:
            result['font'] = self.font
        if self.font_color is not None:
            result['fontColor'] = self.font_color
        if self.font_size is not None:
            result['fontSize'] = self.font_size
        if self.max_char_length is not None:
            result['maxCharLength'] = self.max_char_length
        if self.position_x is not None:
            result['positionX'] = self.position_x
        if self.position_y is not None:
            result['positionY'] = self.position_y
        if self.text_height is not None:
            result['textHeight'] = self.text_height
        if self.text_width is not None:
            result['textWidth'] = self.text_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignment') is not None:
            self.alignment = m.get('alignment')
        if m.get('backgroundColor') is not None:
            self.background_color = m.get('backgroundColor')
        if m.get('font') is not None:
            self.font = m.get('font')
        if m.get('fontColor') is not None:
            self.font_color = m.get('fontColor')
        if m.get('fontSize') is not None:
            self.font_size = m.get('fontSize')
        if m.get('maxCharLength') is not None:
            self.max_char_length = m.get('maxCharLength')
        if m.get('positionX') is not None:
            self.position_x = m.get('positionX')
        if m.get('positionY') is not None:
            self.position_y = m.get('positionY')
        if m.get('textHeight') is not None:
            self.text_height = m.get('textHeight')
        if m.get('textWidth') is not None:
            self.text_width = m.get('textWidth')
        return self


class SubmitProjectTaskRequestFramesVideoScript(TeaModel):
    def __init__(
        self,
        audio_url: str = None,
        speed_rate: str = None,
        text_content: str = None,
        type: str = None,
        voice_template_id: int = None,
        volume: int = None,
    ):
        self.audio_url = audio_url
        self.speed_rate = speed_rate
        self.text_content = text_content
        self.type = type
        self.voice_template_id = voice_template_id
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_url is not None:
            result['audioUrl'] = self.audio_url
        if self.speed_rate is not None:
            result['speedRate'] = self.speed_rate
        if self.text_content is not None:
            result['textContent'] = self.text_content
        if self.type is not None:
            result['type'] = self.type
        if self.voice_template_id is not None:
            result['voiceTemplateId'] = self.voice_template_id
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioUrl') is not None:
            self.audio_url = m.get('audioUrl')
        if m.get('speedRate') is not None:
            self.speed_rate = m.get('speedRate')
        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('voiceTemplateId') is not None:
            self.voice_template_id = m.get('voiceTemplateId')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        return self


class SubmitProjectTaskRequestFrames(TeaModel):
    def __init__(
        self,
        index: int = None,
        layers: List[SubmitProjectTaskRequestFramesLayers] = None,
        subtitle: SubmitProjectTaskRequestFramesSubtitle = None,
        video_script: SubmitProjectTaskRequestFramesVideoScript = None,
    ):
        self.index = index
        self.layers = layers
        self.subtitle = subtitle
        self.video_script = video_script

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video_script:
            self.video_script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.subtitle is not None:
            result['subtitle'] = self.subtitle.to_map()
        if self.video_script is not None:
            result['videoScript'] = self.video_script.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = SubmitProjectTaskRequestFramesLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('subtitle') is not None:
            temp_model = SubmitProjectTaskRequestFramesSubtitle()
            self.subtitle = temp_model.from_map(m['subtitle'])
        if m.get('videoScript') is not None:
            temp_model = SubmitProjectTaskRequestFramesVideoScript()
            self.video_script = temp_model.from_map(m['videoScript'])
        return self


class SubmitProjectTaskRequest(TeaModel):
    def __init__(
        self,
        frames: List[SubmitProjectTaskRequestFrames] = None,
        scale_type: str = None,
        subtitle_tag: int = None,
        transparent_background: int = None,
    ):
        # frame
        self.frames = frames
        self.scale_type = scale_type
        self.subtitle_tag = subtitle_tag
        self.transparent_background = transparent_background

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['frames'].append(k.to_map() if k else None)
        if self.scale_type is not None:
            result['scaleType'] = self.scale_type
        if self.subtitle_tag is not None:
            result['subtitleTag'] = self.subtitle_tag
        if self.transparent_background is not None:
            result['transparentBackground'] = self.transparent_background
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frames = []
        if m.get('frames') is not None:
            for k in m.get('frames'):
                temp_model = SubmitProjectTaskRequestFrames()
                self.frames.append(temp_model.from_map(k))
        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')
        if m.get('subtitleTag') is not None:
            self.subtitle_tag = m.get('subtitleTag')
        if m.get('transparentBackground') is not None:
            self.transparent_background = m.get('transparentBackground')
        return self


class SubmitProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitProjectTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


