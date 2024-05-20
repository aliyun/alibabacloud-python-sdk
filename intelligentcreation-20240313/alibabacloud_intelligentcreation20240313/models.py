# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


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
        desc: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        illustration_task_id_list: List[int] = None,
        text_content: str = None,
        text_id: int = None,
        text_illustration_tag: bool = None,
        text_mode_type: str = None,
        text_status: str = None,
        text_task_id: int = None,
        title: str = None,
        user_name_create: str = None,
        user_name_modified: str = None,
    ):
        # This parameter is required.
        self.desc = desc
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.illustration_task_id_list = illustration_task_id_list
        self.text_content = text_content
        # This parameter is required.
        self.text_id = text_id
        self.text_illustration_tag = text_illustration_tag
        self.text_mode_type = text_mode_type
        # This parameter is required.
        self.text_status = text_status
        # This parameter is required.
        self.text_task_id = text_task_id
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
        if self.desc is not None:
            result['desc'] = self.desc
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.illustration_task_id_list is not None:
            result['illustrationTaskIdList'] = self.illustration_task_id_list
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
        if self.text_task_id is not None:
            result['textTaskId'] = self.text_task_id
        if self.title is not None:
            result['title'] = self.title
        if self.user_name_create is not None:
            result['userNameCreate'] = self.user_name_create
        if self.user_name_modified is not None:
            result['userNameModified'] = self.user_name_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('illustrationTaskIdList') is not None:
            self.illustration_task_id_list = m.get('illustrationTaskIdList')
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
        if m.get('textTaskId') is not None:
            self.text_task_id = m.get('textTaskId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userNameCreate') is not None:
            self.user_name_create = m.get('userNameCreate')
        if m.get('userNameModified') is not None:
            self.user_name_modified = m.get('userNameModified')
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
        theme: str = None,
        theme_desc: str = None,
    ):
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
        self.theme = theme
        self.theme_desc = theme_desc

    def validate(self):
        if self.reference_tag:
            self.reference_tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.theme is not None:
            result['theme'] = self.theme
        if self.theme_desc is not None:
            result['themeDesc'] = self.theme_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('theme') is not None:
            self.theme = m.get('theme')
        if m.get('themeDesc') is not None:
            self.theme_desc = m.get('themeDesc')
        return self


class TextTaskCreateCmd(TeaModel):
    def __init__(
        self,
        content_requirement: str = None,
        idempotent_id: str = None,
        introduction: str = None,
        number: int = None,
        point: str = None,
        reference_tag: ReferenceTag = None,
        related_rag_ids: List[int] = None,
        style: str = None,
        target: str = None,
        text_mode_type: str = None,
        theme: str = None,
    ):
        self.content_requirement = content_requirement
        self.idempotent_id = idempotent_id
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

    def validate(self):
        if self.reference_tag:
            self.reference_tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_requirement is not None:
            result['contentRequirement'] = self.content_requirement
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentRequirement') is not None:
            self.content_requirement = m.get('contentRequirement')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
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


