# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddDocumentInfo(TeaModel):
    def __init__(
        self,
        document_type: str = None,
        name: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.document_type = document_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_type is not None:
            result['documentType'] = self.document_type
        if self.name is not None:
            result['name'] = self.name
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class DocumentInfo(TeaModel):
    def __init__(
        self,
        document_type: str = None,
        id: str = None,
        name: str = None,
        process_status: str = None,
    ):
        self.document_type = document_type
        self.id = id
        self.name = name
        self.process_status = process_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_type is not None:
            result['documentType'] = self.document_type
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.process_status is not None:
            result['processStatus'] = self.process_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processStatus') is not None:
            self.process_status = m.get('processStatus')
        return self


class AddDocumentResult(TeaModel):
    def __init__(
        self,
        doc_name: str = None,
        document_info: DocumentInfo = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.doc_name = doc_name
        self.document_info = document_info
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.document_info:
            self.document_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.document_info is not None:
            result['documentInfo'] = self.document_info.to_map()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('documentInfo') is not None:
            temp_model = DocumentInfo()
            self.document_info = temp_model.from_map(m['documentInfo'])
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AnchorResponse(TeaModel):
    def __init__(
        self,
        anchor_category: str = None,
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
        support_bg_change: int = None,
        use_scene: str = None,
    ):
        self.anchor_category = anchor_category
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
        self.support_bg_change = support_bg_change
        self.use_scene = use_scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_category is not None:
            result['anchorCategory'] = self.anchor_category
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
        if self.support_bg_change is not None:
            result['supportBgChange'] = self.support_bg_change
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorCategory') is not None:
            self.anchor_category = m.get('anchorCategory')
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
        if m.get('supportBgChange') is not None:
            self.support_bg_change = m.get('supportBgChange')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        return self


class BatchAddDocumentResult(TeaModel):
    def __init__(
        self,
        add_document_results: List[AddDocumentResult] = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.add_document_results = add_document_results
        self.request_id = request_id

    def validate(self):
        if self.add_document_results:
            for k in self.add_document_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['addDocumentResults'] = []
        if self.add_document_results is not None:
            for k in self.add_document_results:
                result['addDocumentResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_document_results = []
        if m.get('addDocumentResults') is not None:
            for k in m.get('addDocumentResults'):
                temp_model = AddDocumentResult()
                self.add_document_results.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DocumentResult(TeaModel):
    def __init__(
        self,
        document_info: DocumentInfo = None,
        request_id: str = None,
    ):
        self.document_info = document_info
        self.request_id = request_id

    def validate(self):
        if self.document_info:
            self.document_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_info is not None:
            result['documentInfo'] = self.document_info.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentInfo') is not None:
            temp_model = DocumentInfo()
            self.document_info = temp_model.from_map(m['documentInfo'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
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
        image_urls: List[str] = None,
        nums: int = None,
        oss_paths: List[str] = None,
        sticker_text: str = None,
    ):
        self.background_type = background_type
        self.dst_height = dst_height
        self.dst_width = dst_width
        self.idempotent_id = idempotent_id
        self.image_urls = image_urls
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
        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls
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
        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')
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


class KnowledgeBaseInfo(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        industry: str = None,
        knowledge_base_type: str = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.industry = industry
        self.knowledge_base_type = knowledge_base_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.industry is not None:
            result['industry'] = self.industry
        if self.knowledge_base_type is not None:
            result['knowledgeBaseType'] = self.knowledge_base_type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('knowledgeBaseType') is not None:
            self.knowledge_base_type = m.get('knowledgeBaseType')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class KnowledgeBaseListResult(TeaModel):
    def __init__(
        self,
        knowledge_bases: List[KnowledgeBaseInfo] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.knowledge_bases = knowledge_bases
        self.request_id = request_id
        # This parameter is required.
        self.total = total

    def validate(self):
        if self.knowledge_bases:
            for k in self.knowledge_bases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['knowledgeBases'] = []
        if self.knowledge_bases is not None:
            for k in self.knowledge_bases:
                result['knowledgeBases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_bases = []
        if m.get('knowledgeBases') is not None:
            for k in m.get('knowledgeBases'):
                temp_model = KnowledgeBaseInfo()
                self.knowledge_bases.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
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
        err_msg: str = None,
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
        self.err_msg = err_msg
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
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
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
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
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
        related_rag_ids: List[int] = None,
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
        self.related_rag_ids = related_rag_ids
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
        if self.related_rag_ids is not None:
            result['relatedRagIds'] = self.related_rag_ids
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
        if m.get('relatedRagIds') is not None:
            self.related_rag_ids = m.get('relatedRagIds')
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
        stream_api: bool = None,
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
        self.stream_api = stream_api
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
        if self.stream_api is not None:
            result['streamApi'] = self.stream_api
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
        if m.get('streamApi') is not None:
            self.stream_api = m.get('streamApi')
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
        tts_version: int = None,
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
        self.tts_version = tts_version
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
        if self.tts_version is not None:
            result['ttsVersion'] = self.tts_version
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
        if m.get('ttsVersion') is not None:
            self.tts_version = m.get('ttsVersion')
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


class BatchAddDocumentRequest(TeaModel):
    def __init__(
        self,
        add_document_infos: List[AddDocumentInfo] = None,
    ):
        self.add_document_infos = add_document_infos

    def validate(self):
        if self.add_document_infos:
            for k in self.add_document_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['addDocumentInfos'] = []
        if self.add_document_infos is not None:
            for k in self.add_document_infos:
                result['addDocumentInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_document_infos = []
        if m.get('addDocumentInfos') is not None:
            for k in m.get('addDocumentInfos'):
                temp_model = AddDocumentInfo()
                self.add_document_infos.append(temp_model.from_map(k))
        return self


class BatchAddDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddDocumentResult = None,
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
            temp_model = BatchAddDocumentResult()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateAICoachTaskRequestStudentList(TeaModel):
    def __init__(
        self,
        student_audio_url: str = None,
        student_id: str = None,
    ):
        self.student_audio_url = student_audio_url
        self.student_id = student_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.student_audio_url is not None:
            result['studentAudioUrl'] = self.student_audio_url
        if self.student_id is not None:
            result['studentId'] = self.student_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('studentAudioUrl') is not None:
            self.student_audio_url = m.get('studentAudioUrl')
        if m.get('studentId') is not None:
            self.student_id = m.get('studentId')
        return self


class BatchCreateAICoachTaskRequest(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        script_record_id: str = None,
        student_ids: List[str] = None,
        student_list: List[BatchCreateAICoachTaskRequestStudentList] = None,
    ):
        self.request_id = request_id
        self.script_record_id = script_record_id
        self.student_ids = student_ids
        self.student_list = student_list

    def validate(self):
        if self.student_list:
            for k in self.student_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id
        if self.student_ids is not None:
            result['studentIds'] = self.student_ids
        result['studentList'] = []
        if self.student_list is not None:
            for k in self.student_list:
                result['studentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')
        if m.get('studentIds') is not None:
            self.student_ids = m.get('studentIds')
        self.student_list = []
        if m.get('studentList') is not None:
            for k in m.get('studentList'):
                temp_model = BatchCreateAICoachTaskRequestStudentList()
                self.student_list.append(temp_model.from_map(k))
        return self


class BatchCreateAICoachTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_ids: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class BatchCreateAICoachTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateAICoachTaskResponseBody = None,
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
            temp_model = BatchCreateAICoachTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetProjectTaskRequest(TeaModel):
    def __init__(
        self,
        task_id_list: List[str] = None,
    ):
        self.task_id_list = task_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id_list is not None:
            result['taskIdList'] = self.task_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIdList') is not None:
            self.task_id_list = m.get('taskIdList')
        return self


class BatchGetProjectTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        task_id_list_shrink: str = None,
    ):
        self.task_id_list_shrink = task_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id_list_shrink is not None:
            result['taskIdList'] = self.task_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIdList') is not None:
            self.task_id_list_shrink = m.get('taskIdList')
        return self


class BatchGetProjectTaskResponseBodyResultList(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        status: str = None,
        task_id: str = None,
        video_download_url: str = None,
        video_duration: int = None,
        video_url: str = None,
    ):
        self.error_msg = error_msg
        self.status = status
        self.task_id = task_id
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
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
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
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('videoDownloadUrl') is not None:
            self.video_download_url = m.get('videoDownloadUrl')
        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class BatchGetProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_list: List[BatchGetProjectTaskResponseBodyResultList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['resultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result_list = []
        if m.get('resultList') is not None:
            for k in m.get('resultList'):
                temp_model = BatchGetProjectTaskResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class BatchGetProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetProjectTaskResponseBody = None,
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
            temp_model = BatchGetProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetTrainTaskRequest(TeaModel):
    def __init__(
        self,
        aliyun_main_id: str = None,
        task_id_list: List[str] = None,
    ):
        self.aliyun_main_id = aliyun_main_id
        self.task_id_list = task_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_main_id is not None:
            result['aliyunMainId'] = self.aliyun_main_id
        if self.task_id_list is not None:
            result['taskIdList'] = self.task_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunMainId') is not None:
            self.aliyun_main_id = m.get('aliyunMainId')
        if m.get('taskIdList') is not None:
            self.task_id_list = m.get('taskIdList')
        return self


class BatchGetTrainTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        aliyun_main_id: str = None,
        task_id_list_shrink: str = None,
    ):
        self.aliyun_main_id = aliyun_main_id
        self.task_id_list_shrink = task_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_main_id is not None:
            result['aliyunMainId'] = self.aliyun_main_id
        if self.task_id_list_shrink is not None:
            result['taskIdList'] = self.task_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunMainId') is not None:
            self.aliyun_main_id = m.get('aliyunMainId')
        if m.get('taskIdList') is not None:
            self.task_id_list_shrink = m.get('taskIdList')
        return self


class BatchGetTrainTaskResponseBodyVoiceListVoiceMaterial(TeaModel):
    def __init__(
        self,
        voice_id: int = None,
        voice_language: str = None,
        voice_url: str = None,
    ):
        self.voice_id = voice_id
        self.voice_language = voice_language
        self.voice_url = voice_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.voice_id is not None:
            result['voiceId'] = self.voice_id
        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language
        if self.voice_url is not None:
            result['voiceUrl'] = self.voice_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('voiceId') is not None:
            self.voice_id = m.get('voiceId')
        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')
        if m.get('voiceUrl') is not None:
            self.voice_url = m.get('voiceUrl')
        return self


class BatchGetTrainTaskResponseBodyVoiceList(TeaModel):
    def __init__(
        self,
        aliyun_sub_id: str = None,
        audit_fail_message: str = None,
        audit_status: str = None,
        create_time: str = None,
        gender: str = None,
        name: str = None,
        res_spec_type: str = None,
        task_id: str = None,
        task_type: str = None,
        train_fail_message: str = None,
        train_status: str = None,
        use_scene: str = None,
        voice_material: BatchGetTrainTaskResponseBodyVoiceListVoiceMaterial = None,
    ):
        self.aliyun_sub_id = aliyun_sub_id
        self.audit_fail_message = audit_fail_message
        self.audit_status = audit_status
        self.create_time = create_time
        self.gender = gender
        self.name = name
        self.res_spec_type = res_spec_type
        self.task_id = task_id
        self.task_type = task_type
        self.train_fail_message = train_fail_message
        self.train_status = train_status
        self.use_scene = use_scene
        self.voice_material = voice_material

    def validate(self):
        if self.voice_material:
            self.voice_material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_sub_id is not None:
            result['aliyunSubId'] = self.aliyun_sub_id
        if self.audit_fail_message is not None:
            result['auditFailMessage'] = self.audit_fail_message
        if self.audit_status is not None:
            result['auditStatus'] = self.audit_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.gender is not None:
            result['gender'] = self.gender
        if self.name is not None:
            result['name'] = self.name
        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.train_fail_message is not None:
            result['trainFailMessage'] = self.train_fail_message
        if self.train_status is not None:
            result['trainStatus'] = self.train_status
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        if self.voice_material is not None:
            result['voiceMaterial'] = self.voice_material.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunSubId') is not None:
            self.aliyun_sub_id = m.get('aliyunSubId')
        if m.get('auditFailMessage') is not None:
            self.audit_fail_message = m.get('auditFailMessage')
        if m.get('auditStatus') is not None:
            self.audit_status = m.get('auditStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('trainFailMessage') is not None:
            self.train_fail_message = m.get('trainFailMessage')
        if m.get('trainStatus') is not None:
            self.train_status = m.get('trainStatus')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        if m.get('voiceMaterial') is not None:
            temp_model = BatchGetTrainTaskResponseBodyVoiceListVoiceMaterial()
            self.voice_material = temp_model.from_map(m['voiceMaterial'])
        return self


class BatchGetTrainTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        voice_list: List[BatchGetTrainTaskResponseBodyVoiceList] = None,
    ):
        self.request_id = request_id
        self.voice_list = voice_list

    def validate(self):
        if self.voice_list:
            for k in self.voice_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['voiceList'] = []
        if self.voice_list is not None:
            for k in self.voice_list:
                result['voiceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.voice_list = []
        if m.get('voiceList') is not None:
            for k in m.get('voiceList'):
                temp_model = BatchGetTrainTaskResponseBodyVoiceList()
                self.voice_list.append(temp_model.from_map(k))
        return self


class BatchGetTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetTrainTaskResponseBody = None,
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
            temp_model = BatchGetTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetVideoClipTaskRequest(TeaModel):
    def __init__(
        self,
        task_id_list: List[str] = None,
    ):
        self.task_id_list = task_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id_list is not None:
            result['taskIdList'] = self.task_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIdList') is not None:
            self.task_id_list = m.get('taskIdList')
        return self


class BatchGetVideoClipTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        task_id_list_shrink: str = None,
    ):
        self.task_id_list_shrink = task_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id_list_shrink is not None:
            result['taskIdList'] = self.task_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIdList') is not None:
            self.task_id_list_shrink = m.get('taskIdList')
        return self


class BatchGetVideoClipTaskResponseBodyTaskListVideoList(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        description: str = None,
        end_time: int = None,
        error_msg: str = None,
        title: str = None,
        video_download_url: str = None,
        video_name: str = None,
        video_url: str = None,
    ):
        self.begin_time = begin_time
        self.description = description
        self.end_time = end_time
        self.error_msg = error_msg
        self.title = title
        self.video_download_url = video_download_url
        self.video_name = video_name
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.title is not None:
            result['title'] = self.title
        if self.video_download_url is not None:
            result['videoDownloadUrl'] = self.video_download_url
        if self.video_name is not None:
            result['videoName'] = self.video_name
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('videoDownloadUrl') is not None:
            self.video_download_url = m.get('videoDownloadUrl')
        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class BatchGetVideoClipTaskResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
        total_duration: float = None,
        total_token: int = None,
        video_list: List[BatchGetVideoClipTaskResponseBodyTaskListVideoList] = None,
    ):
        self.status = status
        self.task_id = task_id
        self.total_duration = total_duration
        self.total_token = total_token
        self.video_list = video_list

    def validate(self):
        if self.video_list:
            for k in self.video_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.total_duration is not None:
            result['totalDuration'] = self.total_duration
        if self.total_token is not None:
            result['totalToken'] = self.total_token
        result['videoList'] = []
        if self.video_list is not None:
            for k in self.video_list:
                result['videoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('totalDuration') is not None:
            self.total_duration = m.get('totalDuration')
        if m.get('totalToken') is not None:
            self.total_token = m.get('totalToken')
        self.video_list = []
        if m.get('videoList') is not None:
            for k in m.get('videoList'):
                temp_model = BatchGetVideoClipTaskResponseBodyTaskListVideoList()
                self.video_list.append(temp_model.from_map(k))
        return self


class BatchGetVideoClipTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[BatchGetVideoClipTaskResponseBodyTaskList] = None,
    ):
        self.request_id = request_id
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['taskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['taskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.task_list = []
        if m.get('taskList') is not None:
            for k in m.get('taskList'):
                temp_model = BatchGetVideoClipTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class BatchGetVideoClipTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetVideoClipTaskResponseBody = None,
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
            temp_model = BatchGetVideoClipTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQueryIndividuationTextRequest(TeaModel):
    def __init__(
        self,
        text_id_list: List[str] = None,
    ):
        self.text_id_list = text_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text_id_list is not None:
            result['textIdList'] = self.text_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('textIdList') is not None:
            self.text_id_list = m.get('textIdList')
        return self


class BatchQueryIndividuationTextShrinkRequest(TeaModel):
    def __init__(
        self,
        text_id_list_shrink: str = None,
    ):
        self.text_id_list_shrink = text_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text_id_list_shrink is not None:
            result['textIdList'] = self.text_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('textIdList') is not None:
            self.text_id_list_shrink = m.get('textIdList')
        return self


class BatchQueryIndividuationTextResponseBodyTextList(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        error_msg: str = None,
        item_id: str = None,
        project_id: str = None,
        status: str = None,
        task_id: str = None,
        text_id: str = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.error_msg = error_msg
        self.item_id = item_id
        self.project_id = project_id
        self.status = status
        self.task_id = task_id
        self.text_id = text_id
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.text_id is not None:
            result['textId'] = self.text_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('textId') is not None:
            self.text_id = m.get('textId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class BatchQueryIndividuationTextResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        text_list: List[BatchQueryIndividuationTextResponseBodyTextList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.text_list = text_list

    def validate(self):
        if self.text_list:
            for k in self.text_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['textList'] = []
        if self.text_list is not None:
            for k in self.text_list:
                result['textList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.text_list = []
        if m.get('textList') is not None:
            for k in m.get('textList'):
                temp_model = BatchQueryIndividuationTextResponseBodyTextList()
                self.text_list.append(temp_model.from_map(k))
        return self


class BatchQueryIndividuationTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchQueryIndividuationTextResponseBody = None,
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
            temp_model = BatchQueryIndividuationTextResponseBody()
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


class CloseAICoachTaskSessionRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        uid: str = None,
    ):
        self.session_id = session_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CloseAICoachTaskSessionResponseBody(TeaModel):
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


class CloseAICoachTaskSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseAICoachTaskSessionResponseBody = None,
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
            temp_model = CloseAICoachTaskSessionResponseBody()
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


class CreateAICoachTaskRequest(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        script_record_id: str = None,
        student_audio_url: str = None,
        student_id: str = None,
    ):
        self.request_id = request_id
        self.script_record_id = script_record_id
        self.student_audio_url = student_audio_url
        self.student_id = student_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id
        if self.student_audio_url is not None:
            result['studentAudioUrl'] = self.student_audio_url
        if self.student_id is not None:
            result['studentId'] = self.student_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')
        if m.get('studentAudioUrl') is not None:
            self.student_audio_url = m.get('studentAudioUrl')
        if m.get('studentId') is not None:
            self.student_id = m.get('studentId')
        return self


class CreateAICoachTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateAICoachTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAICoachTaskResponseBody = None,
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
            temp_model = CreateAICoachTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAICoachTaskSessionRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        uid: str = None,
    ):
        self.task_id = task_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateAICoachTaskSessionResponseBodyScriptInfo(TeaModel):
    def __init__(
        self,
        agent_icon_url: str = None,
        character_name: str = None,
        dialogue_text_flag: bool = None,
        dialogue_tip_flag: bool = None,
        initiator: str = None,
        input_type_list: List[str] = None,
        max_duration: int = None,
        script_desc: str = None,
        script_name: str = None,
        script_record_id: str = None,
        script_type: int = None,
        sparring_tip_content: str = None,
        sparring_tip_title: str = None,
        student_think_time_flag: bool = None,
        student_think_time_limit: int = None,
    ):
        self.agent_icon_url = agent_icon_url
        self.character_name = character_name
        self.dialogue_text_flag = dialogue_text_flag
        self.dialogue_tip_flag = dialogue_tip_flag
        self.initiator = initiator
        self.input_type_list = input_type_list
        self.max_duration = max_duration
        self.script_desc = script_desc
        self.script_name = script_name
        self.script_record_id = script_record_id
        self.script_type = script_type
        self.sparring_tip_content = sparring_tip_content
        self.sparring_tip_title = sparring_tip_title
        self.student_think_time_flag = student_think_time_flag
        self.student_think_time_limit = student_think_time_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_icon_url is not None:
            result['agentIconUrl'] = self.agent_icon_url
        if self.character_name is not None:
            result['characterName'] = self.character_name
        if self.dialogue_text_flag is not None:
            result['dialogueTextFlag'] = self.dialogue_text_flag
        if self.dialogue_tip_flag is not None:
            result['dialogueTipFlag'] = self.dialogue_tip_flag
        if self.initiator is not None:
            result['initiator'] = self.initiator
        if self.input_type_list is not None:
            result['inputTypeList'] = self.input_type_list
        if self.max_duration is not None:
            result['maxDuration'] = self.max_duration
        if self.script_desc is not None:
            result['scriptDesc'] = self.script_desc
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id
        if self.script_type is not None:
            result['scriptType'] = self.script_type
        if self.sparring_tip_content is not None:
            result['sparringTipContent'] = self.sparring_tip_content
        if self.sparring_tip_title is not None:
            result['sparringTipTitle'] = self.sparring_tip_title
        if self.student_think_time_flag is not None:
            result['studentThinkTimeFlag'] = self.student_think_time_flag
        if self.student_think_time_limit is not None:
            result['studentThinkTimeLimit'] = self.student_think_time_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentIconUrl') is not None:
            self.agent_icon_url = m.get('agentIconUrl')
        if m.get('characterName') is not None:
            self.character_name = m.get('characterName')
        if m.get('dialogueTextFlag') is not None:
            self.dialogue_text_flag = m.get('dialogueTextFlag')
        if m.get('dialogueTipFlag') is not None:
            self.dialogue_tip_flag = m.get('dialogueTipFlag')
        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')
        if m.get('inputTypeList') is not None:
            self.input_type_list = m.get('inputTypeList')
        if m.get('maxDuration') is not None:
            self.max_duration = m.get('maxDuration')
        if m.get('scriptDesc') is not None:
            self.script_desc = m.get('scriptDesc')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')
        if m.get('scriptType') is not None:
            self.script_type = m.get('scriptType')
        if m.get('sparringTipContent') is not None:
            self.sparring_tip_content = m.get('sparringTipContent')
        if m.get('sparringTipTitle') is not None:
            self.sparring_tip_title = m.get('sparringTipTitle')
        if m.get('studentThinkTimeFlag') is not None:
            self.student_think_time_flag = m.get('studentThinkTimeFlag')
        if m.get('studentThinkTimeLimit') is not None:
            self.student_think_time_limit = m.get('studentThinkTimeLimit')
        return self


class CreateAICoachTaskSessionResponseBody(TeaModel):
    def __init__(
        self,
        channel_token: str = None,
        request_id: str = None,
        script_info: CreateAICoachTaskSessionResponseBodyScriptInfo = None,
        session_id: str = None,
        session_status: int = None,
        token: str = None,
        web_socket_url: str = None,
    ):
        # rtctoken
        self.channel_token = channel_token
        self.request_id = request_id
        self.script_info = script_info
        self.session_id = session_id
        self.session_status = session_status
        # Token
        self.token = token
        self.web_socket_url = web_socket_url

    def validate(self):
        if self.script_info:
            self.script_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_token is not None:
            result['channelToken'] = self.channel_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.script_info is not None:
            result['scriptInfo'] = self.script_info.to_map()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.session_status is not None:
            result['sessionStatus'] = self.session_status
        if self.token is not None:
            result['token'] = self.token
        if self.web_socket_url is not None:
            result['webSocketUrl'] = self.web_socket_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToken') is not None:
            self.channel_token = m.get('channelToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('scriptInfo') is not None:
            temp_model = CreateAICoachTaskSessionResponseBodyScriptInfo()
            self.script_info = temp_model.from_map(m['scriptInfo'])
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('webSocketUrl') is not None:
            self.web_socket_url = m.get('webSocketUrl')
        return self


class CreateAICoachTaskSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAICoachTaskSessionResponseBody = None,
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
            temp_model = CreateAICoachTaskSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAnchorRequest(TeaModel):
    def __init__(
        self,
        anchor_category: str = None,
        anchor_material_name: str = None,
        cover_url: str = None,
        digital_human_type: str = None,
        gender: str = None,
        use_scene: str = None,
        video_oss_key: str = None,
    ):
        self.anchor_category = anchor_category
        self.anchor_material_name = anchor_material_name
        self.cover_url = cover_url
        self.digital_human_type = digital_human_type
        self.gender = gender
        self.use_scene = use_scene
        self.video_oss_key = video_oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_category is not None:
            result['anchorCategory'] = self.anchor_category
        if self.anchor_material_name is not None:
            result['anchorMaterialName'] = self.anchor_material_name
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.digital_human_type is not None:
            result['digitalHumanType'] = self.digital_human_type
        if self.gender is not None:
            result['gender'] = self.gender
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        if self.video_oss_key is not None:
            result['videoOssKey'] = self.video_oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorCategory') is not None:
            self.anchor_category = m.get('anchorCategory')
        if m.get('anchorMaterialName') is not None:
            self.anchor_material_name = m.get('anchorMaterialName')
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('digitalHumanType') is not None:
            self.digital_human_type = m.get('digitalHumanType')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        if m.get('videoOssKey') is not None:
            self.video_oss_key = m.get('videoOssKey')
        return self


class CreateAnchorResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 123456789
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateAnchorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAnchorResponseBody = None,
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
            temp_model = CreateAnchorResponseBody()
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


class CreateIndividuationProjectRequest(TeaModel):
    def __init__(
        self,
        project_info: str = None,
        project_name: str = None,
        purpose: str = None,
        scene_id: str = None,
    ):
        self.project_info = project_info
        self.project_name = project_name
        self.purpose = purpose
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_info is not None:
            result['projectInfo'] = self.project_info
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.purpose is not None:
            result['purpose'] = self.purpose
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectInfo') is not None:
            self.project_info = m.get('projectInfo')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('purpose') is not None:
            self.purpose = m.get('purpose')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class CreateIndividuationProjectResponseBody(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        request_id: str = None,
    ):
        self.project_id = project_id
        # Id of the request
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


class CreateIndividuationProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIndividuationProjectResponseBody = None,
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
            temp_model = CreateIndividuationProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndividuationTextTaskRequest(TeaModel):
    def __init__(
        self,
        crowd_pack: List[List[str]] = None,
        project_id: str = None,
        task_name: str = None,
    ):
        self.crowd_pack = crowd_pack
        self.project_id = project_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crowd_pack is not None:
            result['crowdPack'] = self.crowd_pack
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crowdPack') is not None:
            self.crowd_pack = m.get('crowdPack')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class CreateIndividuationTextTaskResponseBody(TeaModel):
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


class CreateIndividuationTextTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIndividuationTextTaskResponseBody = None,
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
            temp_model = CreateIndividuationTextTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductImageRequest(TeaModel):
    def __init__(
        self,
        background_description: str = None,
        background_priority: int = None,
        background_url: str = None,
        highlight_text: str = None,
        image_count: int = None,
        image_url: str = None,
        sub_title: str = None,
        title: str = None,
    ):
        self.background_description = background_description
        self.background_priority = background_priority
        self.background_url = background_url
        self.highlight_text = highlight_text
        self.image_count = image_count
        self.image_url = image_url
        self.sub_title = sub_title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.background_description is not None:
            result['backgroundDescription'] = self.background_description
        if self.background_priority is not None:
            result['backgroundPriority'] = self.background_priority
        if self.background_url is not None:
            result['backgroundUrl'] = self.background_url
        if self.highlight_text is not None:
            result['highlightText'] = self.highlight_text
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.sub_title is not None:
            result['subTitle'] = self.sub_title
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backgroundDescription') is not None:
            self.background_description = m.get('backgroundDescription')
        if m.get('backgroundPriority') is not None:
            self.background_priority = m.get('backgroundPriority')
        if m.get('backgroundUrl') is not None:
            self.background_url = m.get('backgroundUrl')
        if m.get('highlightText') is not None:
            self.highlight_text = m.get('highlightText')
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('subTitle') is not None:
            self.sub_title = m.get('subTitle')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreateProductImageResponseBody(TeaModel):
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


class CreateProductImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductImageResponseBody = None,
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
            temp_model = CreateProductImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealisticPortraitRequest(TeaModel):
    def __init__(
        self,
        ages: List[int] = None,
        cloth: int = None,
        color: int = None,
        custom: str = None,
        face: List[int] = None,
        figure: int = None,
        gender: int = None,
        hair_color: int = None,
        hairstyle: int = None,
        height: int = None,
        image_url: str = None,
        numbers: int = None,
        ratio: str = None,
        width: int = None,
    ):
        self.ages = ages
        self.cloth = cloth
        self.color = color
        self.custom = custom
        self.face = face
        self.figure = figure
        self.gender = gender
        self.hair_color = hair_color
        self.hairstyle = hairstyle
        self.height = height
        self.image_url = image_url
        self.numbers = numbers
        self.ratio = ratio
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ages is not None:
            result['ages'] = self.ages
        if self.cloth is not None:
            result['cloth'] = self.cloth
        if self.color is not None:
            result['color'] = self.color
        if self.custom is not None:
            result['custom'] = self.custom
        if self.face is not None:
            result['face'] = self.face
        if self.figure is not None:
            result['figure'] = self.figure
        if self.gender is not None:
            result['gender'] = self.gender
        if self.hair_color is not None:
            result['hairColor'] = self.hair_color
        if self.hairstyle is not None:
            result['hairstyle'] = self.hairstyle
        if self.height is not None:
            result['height'] = self.height
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.numbers is not None:
            result['numbers'] = self.numbers
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ages') is not None:
            self.ages = m.get('ages')
        if m.get('cloth') is not None:
            self.cloth = m.get('cloth')
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('custom') is not None:
            self.custom = m.get('custom')
        if m.get('face') is not None:
            self.face = m.get('face')
        if m.get('figure') is not None:
            self.figure = m.get('figure')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('hairColor') is not None:
            self.hair_color = m.get('hairColor')
        if m.get('hairstyle') is not None:
            self.hairstyle = m.get('hairstyle')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('numbers') is not None:
            self.numbers = m.get('numbers')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class CreateRealisticPortraitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
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


class CreateRealisticPortraitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRealisticPortraitResponseBody = None,
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
            temp_model = CreateRealisticPortraitResponseBody()
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


class CreateTrainTaskRequest(TeaModel):
    def __init__(
        self,
        aliyun_main_id: str = None,
        res_spec_type: str = None,
        task_type: str = None,
        use_scene: str = None,
        voice_gender: str = None,
        voice_language: str = None,
        voice_name: str = None,
        voice_path: str = None,
    ):
        self.aliyun_main_id = aliyun_main_id
        self.res_spec_type = res_spec_type
        self.task_type = task_type
        self.use_scene = use_scene
        self.voice_gender = voice_gender
        self.voice_language = voice_language
        self.voice_name = voice_name
        self.voice_path = voice_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_main_id is not None:
            result['aliyunMainId'] = self.aliyun_main_id
        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        if self.voice_gender is not None:
            result['voiceGender'] = self.voice_gender
        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language
        if self.voice_name is not None:
            result['voiceName'] = self.voice_name
        if self.voice_path is not None:
            result['voicePath'] = self.voice_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunMainId') is not None:
            self.aliyun_main_id = m.get('aliyunMainId')
        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        if m.get('voiceGender') is not None:
            self.voice_gender = m.get('voiceGender')
        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')
        if m.get('voiceName') is not None:
            self.voice_name = m.get('voiceName')
        if m.get('voicePath') is not None:
            self.voice_path = m.get('voicePath')
        return self


class CreateTrainTaskResponseBody(TeaModel):
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


class CreateTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrainTaskResponseBody = None,
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
            temp_model = CreateTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoClipTaskRequest(TeaModel):
    def __init__(
        self,
        aliyun_main_id: str = None,
        description: str = None,
        oss_keys: List[str] = None,
        requirement: str = None,
    ):
        self.aliyun_main_id = aliyun_main_id
        self.description = description
        self.oss_keys = oss_keys
        self.requirement = requirement

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_main_id is not None:
            result['aliyunMainId'] = self.aliyun_main_id
        if self.description is not None:
            result['description'] = self.description
        if self.oss_keys is not None:
            result['ossKeys'] = self.oss_keys
        if self.requirement is not None:
            result['requirement'] = self.requirement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunMainId') is not None:
            self.aliyun_main_id = m.get('aliyunMainId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ossKeys') is not None:
            self.oss_keys = m.get('ossKeys')
        if m.get('requirement') is not None:
            self.requirement = m.get('requirement')
        return self


class CreateVideoClipTaskResponseBody(TeaModel):
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


class CreateVideoClipTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVideoClipTaskResponseBody = None,
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
            temp_model = CreateVideoClipTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndividuationProjectRequest(TeaModel):
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


class DeleteIndividuationProjectResponseBody(TeaModel):
    def __init__(
        self,
        desc: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.desc = desc
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DeleteIndividuationProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIndividuationProjectResponseBody = None,
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
            temp_model = DeleteIndividuationProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndividuationTextRequest(TeaModel):
    def __init__(
        self,
        text_id_list: List[str] = None,
    ):
        self.text_id_list = text_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text_id_list is not None:
            result['textIdList'] = self.text_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('textIdList') is not None:
            self.text_id_list = m.get('textIdList')
        return self


class DeleteIndividuationTextResponseBody(TeaModel):
    def __init__(
        self,
        desc: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.desc = desc
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DeleteIndividuationTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIndividuationTextResponseBody = None,
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
            temp_model = DeleteIndividuationTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DocumentResult = None,
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
            temp_model = DocumentResult()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishAICoachTaskSessionRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        uid: str = None,
    ):
        self.session_id = session_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class FinishAICoachTaskSessionResponseBody(TeaModel):
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


class FinishAICoachTaskSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FinishAICoachTaskSessionResponseBody = None,
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
            temp_model = FinishAICoachTaskSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAICoachAssessmentPointRequest(TeaModel):
    def __init__(
        self,
        point_id: str = None,
    ):
        self.point_id = point_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point_id is not None:
            result['pointId'] = self.point_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pointId') is not None:
            self.point_id = m.get('pointId')
        return self


class GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesKeywordValues(TeaModel):
    def __init__(
        self,
        name: str = None,
        weight: int = None,
    ):
        self.name = name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesScoringRules(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetAICoachAssessmentPointResponseBodyAnswerListAnswerValues(TeaModel):
    def __init__(
        self,
        answer_name: str = None,
        answer_weight: int = None,
        keyword_values: List[GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesKeywordValues] = None,
        keyword_weight: int = None,
        scoring_rules: List[GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesScoringRules] = None,
    ):
        self.answer_name = answer_name
        self.answer_weight = answer_weight
        self.keyword_values = keyword_values
        self.keyword_weight = keyword_weight
        self.scoring_rules = scoring_rules

    def validate(self):
        if self.keyword_values:
            for k in self.keyword_values:
                if k:
                    k.validate()
        if self.scoring_rules:
            for k in self.scoring_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_name is not None:
            result['answerName'] = self.answer_name
        if self.answer_weight is not None:
            result['answerWeight'] = self.answer_weight
        result['keywordValues'] = []
        if self.keyword_values is not None:
            for k in self.keyword_values:
                result['keywordValues'].append(k.to_map() if k else None)
        if self.keyword_weight is not None:
            result['keywordWeight'] = self.keyword_weight
        result['scoringRules'] = []
        if self.scoring_rules is not None:
            for k in self.scoring_rules:
                result['scoringRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerName') is not None:
            self.answer_name = m.get('answerName')
        if m.get('answerWeight') is not None:
            self.answer_weight = m.get('answerWeight')
        self.keyword_values = []
        if m.get('keywordValues') is not None:
            for k in m.get('keywordValues'):
                temp_model = GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesKeywordValues()
                self.keyword_values.append(temp_model.from_map(k))
        if m.get('keywordWeight') is not None:
            self.keyword_weight = m.get('keywordWeight')
        self.scoring_rules = []
        if m.get('scoringRules') is not None:
            for k in m.get('scoringRules'):
                temp_model = GetAICoachAssessmentPointResponseBodyAnswerListAnswerValuesScoringRules()
                self.scoring_rules.append(temp_model.from_map(k))
        return self


class GetAICoachAssessmentPointResponseBodyAnswerListParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetAICoachAssessmentPointResponseBodyAnswerList(TeaModel):
    def __init__(
        self,
        answer_values: List[GetAICoachAssessmentPointResponseBodyAnswerListAnswerValues] = None,
        enabled_keyword: bool = None,
        name_list: List[str] = None,
        operators: str = None,
        parameters: List[GetAICoachAssessmentPointResponseBodyAnswerListParameters] = None,
        type: str = None,
        weight: int = None,
    ):
        self.answer_values = answer_values
        self.enabled_keyword = enabled_keyword
        self.name_list = name_list
        self.operators = operators
        self.parameters = parameters
        self.type = type
        self.weight = weight

    def validate(self):
        if self.answer_values:
            for k in self.answer_values:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['answerValues'] = []
        if self.answer_values is not None:
            for k in self.answer_values:
                result['answerValues'].append(k.to_map() if k else None)
        if self.enabled_keyword is not None:
            result['enabledKeyword'] = self.enabled_keyword
        if self.name_list is not None:
            result['nameList'] = self.name_list
        if self.operators is not None:
            result['operators'] = self.operators
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_values = []
        if m.get('answerValues') is not None:
            for k in m.get('answerValues'):
                temp_model = GetAICoachAssessmentPointResponseBodyAnswerListAnswerValues()
                self.answer_values.append(temp_model.from_map(k))
        if m.get('enabledKeyword') is not None:
            self.enabled_keyword = m.get('enabledKeyword')
        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')
        if m.get('operators') is not None:
            self.operators = m.get('operators')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetAICoachAssessmentPointResponseBodyAnswerListParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetAICoachAssessmentPointResponseBody(TeaModel):
    def __init__(
        self,
        answer_list: List[GetAICoachAssessmentPointResponseBodyAnswerList] = None,
        citations: int = None,
        document_id: str = None,
        document_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        kb_id: str = None,
        kb_type: str = None,
        knowledge_list: List[str] = None,
        name: str = None,
        point_id: str = None,
        question_description: str = None,
        question_sample: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.answer_list = answer_list
        self.citations = citations
        self.document_id = document_id
        self.document_name = document_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.kb_id = kb_id
        self.kb_type = kb_type
        self.knowledge_list = knowledge_list
        self.name = name
        self.point_id = point_id
        self.question_description = question_description
        self.question_sample = question_sample
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.answer_list:
            for k in self.answer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['answerList'] = []
        if self.answer_list is not None:
            for k in self.answer_list:
                result['answerList'].append(k.to_map() if k else None)
        if self.citations is not None:
            result['citations'] = self.citations
        if self.document_id is not None:
            result['documentId'] = self.document_id
        if self.document_name is not None:
            result['documentName'] = self.document_name
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.kb_id is not None:
            result['kbId'] = self.kb_id
        if self.kb_type is not None:
            result['kbType'] = self.kb_type
        if self.knowledge_list is not None:
            result['knowledgeList'] = self.knowledge_list
        if self.name is not None:
            result['name'] = self.name
        if self.point_id is not None:
            result['pointId'] = self.point_id
        if self.question_description is not None:
            result['questionDescription'] = self.question_description
        if self.question_sample is not None:
            result['questionSample'] = self.question_sample
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_list = []
        if m.get('answerList') is not None:
            for k in m.get('answerList'):
                temp_model = GetAICoachAssessmentPointResponseBodyAnswerList()
                self.answer_list.append(temp_model.from_map(k))
        if m.get('citations') is not None:
            self.citations = m.get('citations')
        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')
        if m.get('documentName') is not None:
            self.document_name = m.get('documentName')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('kbId') is not None:
            self.kb_id = m.get('kbId')
        if m.get('kbType') is not None:
            self.kb_type = m.get('kbType')
        if m.get('knowledgeList') is not None:
            self.knowledge_list = m.get('knowledgeList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pointId') is not None:
            self.point_id = m.get('pointId')
        if m.get('questionDescription') is not None:
            self.question_description = m.get('questionDescription')
        if m.get('questionSample') is not None:
            self.question_sample = m.get('questionSample')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetAICoachAssessmentPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAICoachAssessmentPointResponseBody = None,
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
            temp_model = GetAICoachAssessmentPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAICoachCheatDetectionRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class GetAICoachCheatDetectionResponseBodyImageCheatList(TeaModel):
    def __init__(
        self,
        time: str = None,
        url: str = None,
    ):
        self.time = time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetAICoachCheatDetectionResponseBodyImageCheat(TeaModel):
    def __init__(
        self,
        desc: str = None,
        list: List[GetAICoachCheatDetectionResponseBodyImageCheatList] = None,
        status: int = None,
    ):
        self.desc = desc
        self.list = list
        self.status = status

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
        if self.desc is not None:
            result['desc'] = self.desc
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetAICoachCheatDetectionResponseBodyImageCheatList()
                self.list.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetAICoachCheatDetectionResponseBodyVoiceCheatComparisonList(TeaModel):
    def __init__(
        self,
        time: str = None,
        url: str = None,
    ):
        self.time = time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetAICoachCheatDetectionResponseBodyVoiceCheatOriginalList(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetAICoachCheatDetectionResponseBodyVoiceCheat(TeaModel):
    def __init__(
        self,
        comparison_list: List[GetAICoachCheatDetectionResponseBodyVoiceCheatComparisonList] = None,
        desc: str = None,
        original_list: List[GetAICoachCheatDetectionResponseBodyVoiceCheatOriginalList] = None,
        status: int = None,
    ):
        self.comparison_list = comparison_list
        self.desc = desc
        self.original_list = original_list
        self.status = status

    def validate(self):
        if self.comparison_list:
            for k in self.comparison_list:
                if k:
                    k.validate()
        if self.original_list:
            for k in self.original_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['comparisonList'] = []
        if self.comparison_list is not None:
            for k in self.comparison_list:
                result['comparisonList'].append(k.to_map() if k else None)
        if self.desc is not None:
            result['desc'] = self.desc
        result['originalList'] = []
        if self.original_list is not None:
            for k in self.original_list:
                result['originalList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comparison_list = []
        if m.get('comparisonList') is not None:
            for k in m.get('comparisonList'):
                temp_model = GetAICoachCheatDetectionResponseBodyVoiceCheatComparisonList()
                self.comparison_list.append(temp_model.from_map(k))
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.original_list = []
        if m.get('originalList') is not None:
            for k in m.get('originalList'):
                temp_model = GetAICoachCheatDetectionResponseBodyVoiceCheatOriginalList()
                self.original_list.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetAICoachCheatDetectionResponseBody(TeaModel):
    def __init__(
        self,
        cheat_id: str = None,
        error_code: str = None,
        error_message: str = None,
        gmt_create: str = None,
        image_cheat: GetAICoachCheatDetectionResponseBodyImageCheat = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
        voice_cheat: GetAICoachCheatDetectionResponseBodyVoiceCheat = None,
    ):
        self.cheat_id = cheat_id
        self.error_code = error_code
        self.error_message = error_message
        self.gmt_create = gmt_create
        self.image_cheat = image_cheat
        # Id of the request
        self.request_id = request_id
        self.status = status
        # true
        self.success = success
        self.voice_cheat = voice_cheat

    def validate(self):
        if self.image_cheat:
            self.image_cheat.validate()
        if self.voice_cheat:
            self.voice_cheat.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cheat_id is not None:
            result['cheatId'] = self.cheat_id
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.image_cheat is not None:
            result['imageCheat'] = self.image_cheat.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        if self.voice_cheat is not None:
            result['voiceCheat'] = self.voice_cheat.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cheatId') is not None:
            self.cheat_id = m.get('cheatId')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('imageCheat') is not None:
            temp_model = GetAICoachCheatDetectionResponseBodyImageCheat()
            self.image_cheat = temp_model.from_map(m['imageCheat'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('voiceCheat') is not None:
            temp_model = GetAICoachCheatDetectionResponseBodyVoiceCheat()
            self.voice_cheat = temp_model.from_map(m['voiceCheat'])
        return self


class GetAICoachCheatDetectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAICoachCheatDetectionResponseBody = None,
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
            temp_model = GetAICoachCheatDetectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAICoachScriptRequest(TeaModel):
    def __init__(
        self,
        script_record_id: str = None,
    ):
        self.script_record_id = script_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')
        return self


class GetAICoachScriptResponseBodyCheckCheatConfig(TeaModel):
    def __init__(
        self,
        check_image: bool = None,
        check_voice: bool = None,
    ):
        self.check_image = check_image
        self.check_voice = check_voice

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_image is not None:
            result['checkImage'] = self.check_image
        if self.check_voice is not None:
            result['checkVoice'] = self.check_voice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkImage') is not None:
            self.check_image = m.get('checkImage')
        if m.get('checkVoice') is not None:
            self.check_voice = m.get('checkVoice')
        return self


class GetAICoachScriptResponseBodyCompleteStrategy(TeaModel):
    def __init__(
        self,
        abnormal_quit_session_expired: int = None,
        abnormal_quit_session_expired_flag: bool = None,
        click_complete_auto_end: bool = None,
        duration: int = None,
        duration_flag: bool = None,
        full_coverage_auto_end: bool = None,
    ):
        self.abnormal_quit_session_expired = abnormal_quit_session_expired
        self.abnormal_quit_session_expired_flag = abnormal_quit_session_expired_flag
        self.click_complete_auto_end = click_complete_auto_end
        self.duration = duration
        self.duration_flag = duration_flag
        self.full_coverage_auto_end = full_coverage_auto_end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_quit_session_expired is not None:
            result['abnormalQuitSessionExpired'] = self.abnormal_quit_session_expired
        if self.abnormal_quit_session_expired_flag is not None:
            result['abnormalQuitSessionExpiredFlag'] = self.abnormal_quit_session_expired_flag
        if self.click_complete_auto_end is not None:
            result['clickCompleteAutoEnd'] = self.click_complete_auto_end
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_flag is not None:
            result['durationFlag'] = self.duration_flag
        if self.full_coverage_auto_end is not None:
            result['fullCoverageAutoEnd'] = self.full_coverage_auto_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abnormalQuitSessionExpired') is not None:
            self.abnormal_quit_session_expired = m.get('abnormalQuitSessionExpired')
        if m.get('abnormalQuitSessionExpiredFlag') is not None:
            self.abnormal_quit_session_expired_flag = m.get('abnormalQuitSessionExpiredFlag')
        if m.get('clickCompleteAutoEnd') is not None:
            self.click_complete_auto_end = m.get('clickCompleteAutoEnd')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationFlag') is not None:
            self.duration_flag = m.get('durationFlag')
        if m.get('fullCoverageAutoEnd') is not None:
            self.full_coverage_auto_end = m.get('fullCoverageAutoEnd')
        return self


class GetAICoachScriptResponseBodyExpressivenessList(TeaModel):
    def __init__(
        self,
        desc: str = None,
        enabled: bool = None,
        expressiveness_id: str = None,
        name: str = None,
        rule: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.desc = desc
        self.enabled = enabled
        self.expressiveness_id = expressiveness_id
        self.name = name
        self.rule = rule
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.expressiveness_id is not None:
            result['expressivenessId'] = self.expressiveness_id
        if self.name is not None:
            result['name'] = self.name
        if self.rule is not None:
            result['rule'] = self.rule
        if self.type is not None:
            result['type'] = self.type
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('expressivenessId') is not None:
            self.expressiveness_id = m.get('expressivenessId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('rule') is not None:
            self.rule = m.get('rule')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetAICoachScriptResponseBodyPointDeductionRuleList(TeaModel):
    def __init__(
        self,
        description: str = None,
        punishment_types: List[str] = None,
        rule_value: str = None,
        weight: int = None,
    ):
        self.description = description
        self.punishment_types = punishment_types
        self.rule_value = rule_value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.punishment_types is not None:
            result['punishmentTypes'] = self.punishment_types
        if self.rule_value is not None:
            result['ruleValue'] = self.rule_value
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('punishmentTypes') is not None:
            self.punishment_types = m.get('punishmentTypes')
        if m.get('ruleValue') is not None:
            self.rule_value = m.get('ruleValue')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesKeywordValues(TeaModel):
    def __init__(
        self,
        name: str = None,
        weight: int = None,
    ):
        self.name = name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesScoringRules(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetAICoachScriptResponseBodyPointsAnswerListAnswerValues(TeaModel):
    def __init__(
        self,
        answer_name: str = None,
        answer_weight: int = None,
        keyword_values: List[GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesKeywordValues] = None,
        keyword_weight: int = None,
        scoring_rules: List[GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesScoringRules] = None,
    ):
        self.answer_name = answer_name
        self.answer_weight = answer_weight
        self.keyword_values = keyword_values
        self.keyword_weight = keyword_weight
        self.scoring_rules = scoring_rules

    def validate(self):
        if self.keyword_values:
            for k in self.keyword_values:
                if k:
                    k.validate()
        if self.scoring_rules:
            for k in self.scoring_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_name is not None:
            result['answerName'] = self.answer_name
        if self.answer_weight is not None:
            result['answerWeight'] = self.answer_weight
        result['keywordValues'] = []
        if self.keyword_values is not None:
            for k in self.keyword_values:
                result['keywordValues'].append(k.to_map() if k else None)
        if self.keyword_weight is not None:
            result['keywordWeight'] = self.keyword_weight
        result['scoringRules'] = []
        if self.scoring_rules is not None:
            for k in self.scoring_rules:
                result['scoringRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerName') is not None:
            self.answer_name = m.get('answerName')
        if m.get('answerWeight') is not None:
            self.answer_weight = m.get('answerWeight')
        self.keyword_values = []
        if m.get('keywordValues') is not None:
            for k in m.get('keywordValues'):
                temp_model = GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesKeywordValues()
                self.keyword_values.append(temp_model.from_map(k))
        if m.get('keywordWeight') is not None:
            self.keyword_weight = m.get('keywordWeight')
        self.scoring_rules = []
        if m.get('scoringRules') is not None:
            for k in m.get('scoringRules'):
                temp_model = GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesScoringRules()
                self.scoring_rules.append(temp_model.from_map(k))
        return self


class GetAICoachScriptResponseBodyPointsAnswerListParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetAICoachScriptResponseBodyPointsAnswerList(TeaModel):
    def __init__(
        self,
        answer_values: List[GetAICoachScriptResponseBodyPointsAnswerListAnswerValues] = None,
        enabled_keyword: bool = None,
        name: str = None,
        name_list: List[str] = None,
        operators: str = None,
        parameters: List[GetAICoachScriptResponseBodyPointsAnswerListParameters] = None,
        type: str = None,
        weight: int = None,
    ):
        self.answer_values = answer_values
        self.enabled_keyword = enabled_keyword
        self.name = name
        self.name_list = name_list
        self.operators = operators
        self.parameters = parameters
        self.type = type
        self.weight = weight

    def validate(self):
        if self.answer_values:
            for k in self.answer_values:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['answerValues'] = []
        if self.answer_values is not None:
            for k in self.answer_values:
                result['answerValues'].append(k.to_map() if k else None)
        if self.enabled_keyword is not None:
            result['enabledKeyword'] = self.enabled_keyword
        if self.name is not None:
            result['name'] = self.name
        if self.name_list is not None:
            result['nameList'] = self.name_list
        if self.operators is not None:
            result['operators'] = self.operators
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_values = []
        if m.get('answerValues') is not None:
            for k in m.get('answerValues'):
                temp_model = GetAICoachScriptResponseBodyPointsAnswerListAnswerValues()
                self.answer_values.append(temp_model.from_map(k))
        if m.get('enabledKeyword') is not None:
            self.enabled_keyword = m.get('enabledKeyword')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')
        if m.get('operators') is not None:
            self.operators = m.get('operators')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetAICoachScriptResponseBodyPointsAnswerListParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetAICoachScriptResponseBodyPoints(TeaModel):
    def __init__(
        self,
        answer_list: List[GetAICoachScriptResponseBodyPointsAnswerList] = None,
        knowledge_list: List[str] = None,
        name: str = None,
        point_id: str = None,
        question_description: str = None,
        sort_no: int = None,
        weight: int = None,
    ):
        self.answer_list = answer_list
        self.knowledge_list = knowledge_list
        self.name = name
        self.point_id = point_id
        self.question_description = question_description
        self.sort_no = sort_no
        self.weight = weight

    def validate(self):
        if self.answer_list:
            for k in self.answer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['answerList'] = []
        if self.answer_list is not None:
            for k in self.answer_list:
                result['answerList'].append(k.to_map() if k else None)
        if self.knowledge_list is not None:
            result['knowledgeList'] = self.knowledge_list
        if self.name is not None:
            result['name'] = self.name
        if self.point_id is not None:
            result['pointId'] = self.point_id
        if self.question_description is not None:
            result['questionDescription'] = self.question_description
        if self.sort_no is not None:
            result['sortNo'] = self.sort_no
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_list = []
        if m.get('answerList') is not None:
            for k in m.get('answerList'):
                temp_model = GetAICoachScriptResponseBodyPointsAnswerList()
                self.answer_list.append(temp_model.from_map(k))
        if m.get('knowledgeList') is not None:
            self.knowledge_list = m.get('knowledgeList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pointId') is not None:
            self.point_id = m.get('pointId')
        if m.get('questionDescription') is not None:
            self.question_description = m.get('questionDescription')
        if m.get('sortNo') is not None:
            self.sort_no = m.get('sortNo')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetAICoachScriptResponseBodySampleDialogueList(TeaModel):
    def __init__(
        self,
        message: str = None,
        role: str = None,
    ):
        self.message = message
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class GetAICoachScriptResponseBodyScoreConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        pass_score: str = None,
    ):
        self.enabled = enabled
        self.pass_score = pass_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.pass_score is not None:
            result['passScore'] = self.pass_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('passScore') is not None:
            self.pass_score = m.get('passScore')
        return self


class GetAICoachScriptResponseBodyWeights(TeaModel):
    def __init__(
        self,
        ability_evaluation: int = None,
        ability_evaluation_enabled: bool = None,
        assessment_point: int = None,
        assessment_point_enabled: bool = None,
        expressiveness: int = None,
        expressiveness_enabled: bool = None,
        point_deduction_rule: int = None,
        point_deduction_rule_enabled: bool = None,
        standard: int = None,
        standard_enabled: bool = None,
    ):
        self.ability_evaluation = ability_evaluation
        self.ability_evaluation_enabled = ability_evaluation_enabled
        self.assessment_point = assessment_point
        self.assessment_point_enabled = assessment_point_enabled
        self.expressiveness = expressiveness
        self.expressiveness_enabled = expressiveness_enabled
        self.point_deduction_rule = point_deduction_rule
        self.point_deduction_rule_enabled = point_deduction_rule_enabled
        self.standard = standard
        self.standard_enabled = standard_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ability_evaluation is not None:
            result['abilityEvaluation'] = self.ability_evaluation
        if self.ability_evaluation_enabled is not None:
            result['abilityEvaluationEnabled'] = self.ability_evaluation_enabled
        if self.assessment_point is not None:
            result['assessmentPoint'] = self.assessment_point
        if self.assessment_point_enabled is not None:
            result['assessmentPointEnabled'] = self.assessment_point_enabled
        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness
        if self.expressiveness_enabled is not None:
            result['expressivenessEnabled'] = self.expressiveness_enabled
        if self.point_deduction_rule is not None:
            result['pointDeductionRule'] = self.point_deduction_rule
        if self.point_deduction_rule_enabled is not None:
            result['pointDeductionRuleEnabled'] = self.point_deduction_rule_enabled
        if self.standard is not None:
            result['standard'] = self.standard
        if self.standard_enabled is not None:
            result['standardEnabled'] = self.standard_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abilityEvaluation') is not None:
            self.ability_evaluation = m.get('abilityEvaluation')
        if m.get('abilityEvaluationEnabled') is not None:
            self.ability_evaluation_enabled = m.get('abilityEvaluationEnabled')
        if m.get('assessmentPoint') is not None:
            self.assessment_point = m.get('assessmentPoint')
        if m.get('assessmentPointEnabled') is not None:
            self.assessment_point_enabled = m.get('assessmentPointEnabled')
        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')
        if m.get('expressivenessEnabled') is not None:
            self.expressiveness_enabled = m.get('expressivenessEnabled')
        if m.get('pointDeductionRule') is not None:
            self.point_deduction_rule = m.get('pointDeductionRule')
        if m.get('pointDeductionRuleEnabled') is not None:
            self.point_deduction_rule_enabled = m.get('pointDeductionRuleEnabled')
        if m.get('standard') is not None:
            self.standard = m.get('standard')
        if m.get('standardEnabled') is not None:
            self.standard_enabled = m.get('standardEnabled')
        return self


class GetAICoachScriptResponseBody(TeaModel):
    def __init__(
        self,
        append_question_flag: bool = None,
        assessment_scope: str = None,
        check_cheat_config: GetAICoachScriptResponseBodyCheckCheatConfig = None,
        closing_remarks: str = None,
        complete_strategy: GetAICoachScriptResponseBodyCompleteStrategy = None,
        cover_url: str = None,
        dialogue_input_text_limit: int = None,
        dialogue_text_flag: bool = None,
        dialogue_tip_flag: bool = None,
        dialogue_voice_limit: int = None,
        evaluate_report_flag: bool = None,
        expressiveness: Dict[str, int] = None,
        expressiveness_list: List[GetAICoachScriptResponseBodyExpressivenessList] = None,
        gif_dynamic_url: str = None,
        gif_static_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        initiator: str = None,
        interaction_input_types: List[str] = None,
        interaction_type: int = None,
        introduce: str = None,
        name: str = None,
        opening_remarks: str = None,
        order_ack_flag: bool = None,
        point_deduction_rule_list: List[GetAICoachScriptResponseBodyPointDeductionRuleList] = None,
        points: List[GetAICoachScriptResponseBodyPoints] = None,
        request_id: str = None,
        sample_dialogue_list: List[GetAICoachScriptResponseBodySampleDialogueList] = None,
        score_config: GetAICoachScriptResponseBodyScoreConfig = None,
        script_record_id: str = None,
        sparring_tip_content: str = None,
        sparring_tip_title: str = None,
        status: int = None,
        student_think_time_flag: bool = None,
        student_think_time_limit: int = None,
        type: int = None,
        weights: GetAICoachScriptResponseBodyWeights = None,
    ):
        self.append_question_flag = append_question_flag
        self.assessment_scope = assessment_scope
        self.check_cheat_config = check_cheat_config
        self.closing_remarks = closing_remarks
        self.complete_strategy = complete_strategy
        self.cover_url = cover_url
        self.dialogue_input_text_limit = dialogue_input_text_limit
        self.dialogue_text_flag = dialogue_text_flag
        self.dialogue_tip_flag = dialogue_tip_flag
        self.dialogue_voice_limit = dialogue_voice_limit
        self.evaluate_report_flag = evaluate_report_flag
        self.expressiveness = expressiveness
        self.expressiveness_list = expressiveness_list
        self.gif_dynamic_url = gif_dynamic_url
        self.gif_static_url = gif_static_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.initiator = initiator
        self.interaction_input_types = interaction_input_types
        self.interaction_type = interaction_type
        self.introduce = introduce
        self.name = name
        self.opening_remarks = opening_remarks
        self.order_ack_flag = order_ack_flag
        self.point_deduction_rule_list = point_deduction_rule_list
        self.points = points
        self.request_id = request_id
        self.sample_dialogue_list = sample_dialogue_list
        self.score_config = score_config
        self.script_record_id = script_record_id
        self.sparring_tip_content = sparring_tip_content
        self.sparring_tip_title = sparring_tip_title
        self.status = status
        self.student_think_time_flag = student_think_time_flag
        self.student_think_time_limit = student_think_time_limit
        self.type = type
        self.weights = weights

    def validate(self):
        if self.check_cheat_config:
            self.check_cheat_config.validate()
        if self.complete_strategy:
            self.complete_strategy.validate()
        if self.expressiveness_list:
            for k in self.expressiveness_list:
                if k:
                    k.validate()
        if self.point_deduction_rule_list:
            for k in self.point_deduction_rule_list:
                if k:
                    k.validate()
        if self.points:
            for k in self.points:
                if k:
                    k.validate()
        if self.sample_dialogue_list:
            for k in self.sample_dialogue_list:
                if k:
                    k.validate()
        if self.score_config:
            self.score_config.validate()
        if self.weights:
            self.weights.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_question_flag is not None:
            result['appendQuestionFlag'] = self.append_question_flag
        if self.assessment_scope is not None:
            result['assessmentScope'] = self.assessment_scope
        if self.check_cheat_config is not None:
            result['checkCheatConfig'] = self.check_cheat_config.to_map()
        if self.closing_remarks is not None:
            result['closingRemarks'] = self.closing_remarks
        if self.complete_strategy is not None:
            result['completeStrategy'] = self.complete_strategy.to_map()
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.dialogue_input_text_limit is not None:
            result['dialogueInputTextLimit'] = self.dialogue_input_text_limit
        if self.dialogue_text_flag is not None:
            result['dialogueTextFlag'] = self.dialogue_text_flag
        if self.dialogue_tip_flag is not None:
            result['dialogueTipFlag'] = self.dialogue_tip_flag
        if self.dialogue_voice_limit is not None:
            result['dialogueVoiceLimit'] = self.dialogue_voice_limit
        if self.evaluate_report_flag is not None:
            result['evaluateReportFlag'] = self.evaluate_report_flag
        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness
        result['expressivenessList'] = []
        if self.expressiveness_list is not None:
            for k in self.expressiveness_list:
                result['expressivenessList'].append(k.to_map() if k else None)
        if self.gif_dynamic_url is not None:
            result['gifDynamicUrl'] = self.gif_dynamic_url
        if self.gif_static_url is not None:
            result['gifStaticUrl'] = self.gif_static_url
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.initiator is not None:
            result['initiator'] = self.initiator
        if self.interaction_input_types is not None:
            result['interactionInputTypes'] = self.interaction_input_types
        if self.interaction_type is not None:
            result['interactionType'] = self.interaction_type
        if self.introduce is not None:
            result['introduce'] = self.introduce
        if self.name is not None:
            result['name'] = self.name
        if self.opening_remarks is not None:
            result['openingRemarks'] = self.opening_remarks
        if self.order_ack_flag is not None:
            result['orderAckFlag'] = self.order_ack_flag
        result['pointDeductionRuleList'] = []
        if self.point_deduction_rule_list is not None:
            for k in self.point_deduction_rule_list:
                result['pointDeductionRuleList'].append(k.to_map() if k else None)
        result['points'] = []
        if self.points is not None:
            for k in self.points:
                result['points'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['sampleDialogueList'] = []
        if self.sample_dialogue_list is not None:
            for k in self.sample_dialogue_list:
                result['sampleDialogueList'].append(k.to_map() if k else None)
        if self.score_config is not None:
            result['scoreConfig'] = self.score_config.to_map()
        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id
        if self.sparring_tip_content is not None:
            result['sparringTipContent'] = self.sparring_tip_content
        if self.sparring_tip_title is not None:
            result['sparringTipTitle'] = self.sparring_tip_title
        if self.status is not None:
            result['status'] = self.status
        if self.student_think_time_flag is not None:
            result['studentThinkTimeFlag'] = self.student_think_time_flag
        if self.student_think_time_limit is not None:
            result['studentThinkTimeLimit'] = self.student_think_time_limit
        if self.type is not None:
            result['type'] = self.type
        if self.weights is not None:
            result['weights'] = self.weights.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendQuestionFlag') is not None:
            self.append_question_flag = m.get('appendQuestionFlag')
        if m.get('assessmentScope') is not None:
            self.assessment_scope = m.get('assessmentScope')
        if m.get('checkCheatConfig') is not None:
            temp_model = GetAICoachScriptResponseBodyCheckCheatConfig()
            self.check_cheat_config = temp_model.from_map(m['checkCheatConfig'])
        if m.get('closingRemarks') is not None:
            self.closing_remarks = m.get('closingRemarks')
        if m.get('completeStrategy') is not None:
            temp_model = GetAICoachScriptResponseBodyCompleteStrategy()
            self.complete_strategy = temp_model.from_map(m['completeStrategy'])
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('dialogueInputTextLimit') is not None:
            self.dialogue_input_text_limit = m.get('dialogueInputTextLimit')
        if m.get('dialogueTextFlag') is not None:
            self.dialogue_text_flag = m.get('dialogueTextFlag')
        if m.get('dialogueTipFlag') is not None:
            self.dialogue_tip_flag = m.get('dialogueTipFlag')
        if m.get('dialogueVoiceLimit') is not None:
            self.dialogue_voice_limit = m.get('dialogueVoiceLimit')
        if m.get('evaluateReportFlag') is not None:
            self.evaluate_report_flag = m.get('evaluateReportFlag')
        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')
        self.expressiveness_list = []
        if m.get('expressivenessList') is not None:
            for k in m.get('expressivenessList'):
                temp_model = GetAICoachScriptResponseBodyExpressivenessList()
                self.expressiveness_list.append(temp_model.from_map(k))
        if m.get('gifDynamicUrl') is not None:
            self.gif_dynamic_url = m.get('gifDynamicUrl')
        if m.get('gifStaticUrl') is not None:
            self.gif_static_url = m.get('gifStaticUrl')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')
        if m.get('interactionInputTypes') is not None:
            self.interaction_input_types = m.get('interactionInputTypes')
        if m.get('interactionType') is not None:
            self.interaction_type = m.get('interactionType')
        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('openingRemarks') is not None:
            self.opening_remarks = m.get('openingRemarks')
        if m.get('orderAckFlag') is not None:
            self.order_ack_flag = m.get('orderAckFlag')
        self.point_deduction_rule_list = []
        if m.get('pointDeductionRuleList') is not None:
            for k in m.get('pointDeductionRuleList'):
                temp_model = GetAICoachScriptResponseBodyPointDeductionRuleList()
                self.point_deduction_rule_list.append(temp_model.from_map(k))
        self.points = []
        if m.get('points') is not None:
            for k in m.get('points'):
                temp_model = GetAICoachScriptResponseBodyPoints()
                self.points.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.sample_dialogue_list = []
        if m.get('sampleDialogueList') is not None:
            for k in m.get('sampleDialogueList'):
                temp_model = GetAICoachScriptResponseBodySampleDialogueList()
                self.sample_dialogue_list.append(temp_model.from_map(k))
        if m.get('scoreConfig') is not None:
            temp_model = GetAICoachScriptResponseBodyScoreConfig()
            self.score_config = temp_model.from_map(m['scoreConfig'])
        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')
        if m.get('sparringTipContent') is not None:
            self.sparring_tip_content = m.get('sparringTipContent')
        if m.get('sparringTipTitle') is not None:
            self.sparring_tip_title = m.get('sparringTipTitle')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('studentThinkTimeFlag') is not None:
            self.student_think_time_flag = m.get('studentThinkTimeFlag')
        if m.get('studentThinkTimeLimit') is not None:
            self.student_think_time_limit = m.get('studentThinkTimeLimit')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('weights') is not None:
            temp_model = GetAICoachScriptResponseBodyWeights()
            self.weights = temp_model.from_map(m['weights'])
        return self


class GetAICoachScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAICoachScriptResponseBody = None,
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
            temp_model = GetAICoachScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAICoachTaskSessionHistoryRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        session_id: str = None,
        uid: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.session_id = session_id
        self.uid = uid

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
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetAICoachTaskSessionHistoryResponseBodyConversationList(TeaModel):
    def __init__(
        self,
        audio_url: str = None,
        evaluation_feedback: str = None,
        evaluation_result: str = None,
        message: str = None,
        record_id: str = None,
        role: str = None,
    ):
        self.audio_url = audio_url
        self.evaluation_feedback = evaluation_feedback
        self.evaluation_result = evaluation_result
        self.message = message
        self.record_id = record_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_url is not None:
            result['audioUrl'] = self.audio_url
        if self.evaluation_feedback is not None:
            result['evaluationFeedback'] = self.evaluation_feedback
        if self.evaluation_result is not None:
            result['evaluationResult'] = self.evaluation_result
        if self.message is not None:
            result['message'] = self.message
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioUrl') is not None:
            self.audio_url = m.get('audioUrl')
        if m.get('evaluationFeedback') is not None:
            self.evaluation_feedback = m.get('evaluationFeedback')
        if m.get('evaluationResult') is not None:
            self.evaluation_result = m.get('evaluationResult')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class GetAICoachTaskSessionHistoryResponseBody(TeaModel):
    def __init__(
        self,
        conversation_list: List[GetAICoachTaskSessionHistoryResponseBodyConversationList] = None,
        duration: int = None,
        end_time: str = None,
        pause_duration: int = None,
        request_id: str = None,
        script_name: str = None,
        start_time: str = None,
        status: str = None,
        total: int = None,
        uid: str = None,
    ):
        self.conversation_list = conversation_list
        self.duration = duration
        self.end_time = end_time
        self.pause_duration = pause_duration
        self.request_id = request_id
        self.script_name = script_name
        self.start_time = start_time
        self.status = status
        self.total = total
        self.uid = uid

    def validate(self):
        if self.conversation_list:
            for k in self.conversation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conversationList'] = []
        if self.conversation_list is not None:
            for k in self.conversation_list:
                result['conversationList'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['duration'] = self.duration
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.pause_duration is not None:
            result['pauseDuration'] = self.pause_duration
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.total is not None:
            result['total'] = self.total
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conversation_list = []
        if m.get('conversationList') is not None:
            for k in m.get('conversationList'):
                temp_model = GetAICoachTaskSessionHistoryResponseBodyConversationList()
                self.conversation_list.append(temp_model.from_map(k))
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pauseDuration') is not None:
            self.pause_duration = m.get('pauseDuration')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetAICoachTaskSessionHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAICoachTaskSessionHistoryResponseBody = None,
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
            temp_model = GetAICoachTaskSessionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAICoachTaskSessionReportRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        uid: str = None,
    ):
        self.session_id = session_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetAICoachTaskSessionReportResponseBody(TeaModel):
    def __init__(
        self,
        duration: int = None,
        end_time: str = None,
        evaluation_rating: str = None,
        evaluation_result: str = None,
        feedback: bool = None,
        request_id: str = None,
        script_name: str = None,
        start_time: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.evaluation_rating = evaluation_rating
        self.evaluation_result = evaluation_result
        self.feedback = feedback
        self.request_id = request_id
        self.script_name = script_name
        self.start_time = start_time
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.evaluation_rating is not None:
            result['evaluationRating'] = self.evaluation_rating
        if self.evaluation_result is not None:
            result['evaluationResult'] = self.evaluation_result
        if self.feedback is not None:
            result['feedback'] = self.feedback
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('evaluationRating') is not None:
            self.evaluation_rating = m.get('evaluationRating')
        if m.get('evaluationResult') is not None:
            self.evaluation_result = m.get('evaluationResult')
        if m.get('feedback') is not None:
            self.feedback = m.get('feedback')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetAICoachTaskSessionReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAICoachTaskSessionReportResponseBody = None,
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
            temp_model = GetAICoachTaskSessionReportResponseBody()
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
        upload_type: int = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_type = file_type
        self.upload_type = upload_type

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
        if self.upload_type is not None:
            result['uploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('uploadType') is not None:
            self.upload_type = m.get('uploadType')
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


class InteractTextRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        content: str = None,
        session_id: str = None,
    ):
        self.agent_id = agent_id
        self.content = content
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.content is not None:
            result['content'] = self.content
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class InteractTextResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        index: int = None,
        message: str = None,
        related_images: List[str] = None,
        related_videos: List[str] = None,
        session_id: str = None,
        type: int = None,
    ):
        self.end = end
        self.index = index
        self.message = message
        self.related_images = related_images
        self.related_videos = related_videos
        self.session_id = session_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.index is not None:
            result['index'] = self.index
        if self.message is not None:
            result['message'] = self.message
        if self.related_images is not None:
            result['relatedImages'] = self.related_images
        if self.related_videos is not None:
            result['relatedVideos'] = self.related_videos
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('relatedImages') is not None:
            self.related_images = m.get('relatedImages')
        if m.get('relatedVideos') is not None:
            self.related_videos = m.get('relatedVideos')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InteractTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InteractTextResponseBody = None,
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
            temp_model = InteractTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAICoachScriptPageRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
        type: int = None,
    ):
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAICoachScriptPageResponseBodyListCompleteStrategy(TeaModel):
    def __init__(
        self,
        click_complete_auto_end: bool = None,
        duration: int = None,
        full_coverage_auto_end: bool = None,
    ):
        self.click_complete_auto_end = click_complete_auto_end
        self.duration = duration
        self.full_coverage_auto_end = full_coverage_auto_end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.click_complete_auto_end is not None:
            result['clickCompleteAutoEnd'] = self.click_complete_auto_end
        if self.duration is not None:
            result['duration'] = self.duration
        if self.full_coverage_auto_end is not None:
            result['fullCoverageAutoEnd'] = self.full_coverage_auto_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clickCompleteAutoEnd') is not None:
            self.click_complete_auto_end = m.get('clickCompleteAutoEnd')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('fullCoverageAutoEnd') is not None:
            self.full_coverage_auto_end = m.get('fullCoverageAutoEnd')
        return self


class ListAICoachScriptPageResponseBodyListSampleDialogueList(TeaModel):
    def __init__(
        self,
        message: str = None,
        role: str = None,
    ):
        self.message = message
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ListAICoachScriptPageResponseBodyListScoreConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        pass_score: int = None,
    ):
        self.enabled = enabled
        self.pass_score = pass_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.pass_score is not None:
            result['passScore'] = self.pass_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('passScore') is not None:
            self.pass_score = m.get('passScore')
        return self


class ListAICoachScriptPageResponseBodyListWeights(TeaModel):
    def __init__(
        self,
        assessment_point: int = None,
        assessment_point_enabled: bool = None,
        expressiveness: int = None,
        expressiveness_enabled: bool = None,
        point_deduction_rule: int = None,
        point_deduction_rule_enabled: bool = None,
        standard: int = None,
        standard_enabled: bool = None,
    ):
        self.assessment_point = assessment_point
        self.assessment_point_enabled = assessment_point_enabled
        self.expressiveness = expressiveness
        self.expressiveness_enabled = expressiveness_enabled
        self.point_deduction_rule = point_deduction_rule
        self.point_deduction_rule_enabled = point_deduction_rule_enabled
        self.standard = standard
        self.standard_enabled = standard_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assessment_point is not None:
            result['assessmentPoint'] = self.assessment_point
        if self.assessment_point_enabled is not None:
            result['assessmentPointEnabled'] = self.assessment_point_enabled
        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness
        if self.expressiveness_enabled is not None:
            result['expressivenessEnabled'] = self.expressiveness_enabled
        if self.point_deduction_rule is not None:
            result['pointDeductionRule'] = self.point_deduction_rule
        if self.point_deduction_rule_enabled is not None:
            result['pointDeductionRuleEnabled'] = self.point_deduction_rule_enabled
        if self.standard is not None:
            result['standard'] = self.standard
        if self.standard_enabled is not None:
            result['standardEnabled'] = self.standard_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assessmentPoint') is not None:
            self.assessment_point = m.get('assessmentPoint')
        if m.get('assessmentPointEnabled') is not None:
            self.assessment_point_enabled = m.get('assessmentPointEnabled')
        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')
        if m.get('expressivenessEnabled') is not None:
            self.expressiveness_enabled = m.get('expressivenessEnabled')
        if m.get('pointDeductionRule') is not None:
            self.point_deduction_rule = m.get('pointDeductionRule')
        if m.get('pointDeductionRuleEnabled') is not None:
            self.point_deduction_rule_enabled = m.get('pointDeductionRuleEnabled')
        if m.get('standard') is not None:
            self.standard = m.get('standard')
        if m.get('standardEnabled') is not None:
            self.standard_enabled = m.get('standardEnabled')
        return self


class ListAICoachScriptPageResponseBodyList(TeaModel):
    def __init__(
        self,
        append_question_flag: str = None,
        assessment_scope: str = None,
        closing_remarks: str = None,
        complete_strategy: ListAICoachScriptPageResponseBodyListCompleteStrategy = None,
        cover_url: str = None,
        dialogue_text_flag: bool = None,
        dialogue_tip_flag: bool = None,
        evaluate_report_flag: bool = None,
        expressiveness: Dict[str, str] = None,
        gif_dynamic_url: str = None,
        gif_static_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        initiator: str = None,
        interaction_type: str = None,
        introduce: str = None,
        name: str = None,
        opening_remarks: str = None,
        order_ack_flag: bool = None,
        sample_dialogue_list: List[ListAICoachScriptPageResponseBodyListSampleDialogueList] = None,
        score_config: ListAICoachScriptPageResponseBodyListScoreConfig = None,
        script_record_id: str = None,
        sparring_tip_content: str = None,
        sparring_tip_title: str = None,
        status: int = None,
        student_think_time_flag: bool = None,
        type: int = None,
        weights: ListAICoachScriptPageResponseBodyListWeights = None,
    ):
        self.append_question_flag = append_question_flag
        self.assessment_scope = assessment_scope
        self.closing_remarks = closing_remarks
        self.complete_strategy = complete_strategy
        self.cover_url = cover_url
        self.dialogue_text_flag = dialogue_text_flag
        self.dialogue_tip_flag = dialogue_tip_flag
        self.evaluate_report_flag = evaluate_report_flag
        self.expressiveness = expressiveness
        self.gif_dynamic_url = gif_dynamic_url
        self.gif_static_url = gif_static_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.initiator = initiator
        self.interaction_type = interaction_type
        self.introduce = introduce
        self.name = name
        self.opening_remarks = opening_remarks
        self.order_ack_flag = order_ack_flag
        self.sample_dialogue_list = sample_dialogue_list
        self.score_config = score_config
        self.script_record_id = script_record_id
        self.sparring_tip_content = sparring_tip_content
        self.sparring_tip_title = sparring_tip_title
        self.status = status
        self.student_think_time_flag = student_think_time_flag
        self.type = type
        self.weights = weights

    def validate(self):
        if self.complete_strategy:
            self.complete_strategy.validate()
        if self.sample_dialogue_list:
            for k in self.sample_dialogue_list:
                if k:
                    k.validate()
        if self.score_config:
            self.score_config.validate()
        if self.weights:
            self.weights.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_question_flag is not None:
            result['appendQuestionFlag'] = self.append_question_flag
        if self.assessment_scope is not None:
            result['assessmentScope'] = self.assessment_scope
        if self.closing_remarks is not None:
            result['closingRemarks'] = self.closing_remarks
        if self.complete_strategy is not None:
            result['completeStrategy'] = self.complete_strategy.to_map()
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url
        if self.dialogue_text_flag is not None:
            result['dialogueTextFlag'] = self.dialogue_text_flag
        if self.dialogue_tip_flag is not None:
            result['dialogueTipFlag'] = self.dialogue_tip_flag
        if self.evaluate_report_flag is not None:
            result['evaluateReportFlag'] = self.evaluate_report_flag
        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness
        if self.gif_dynamic_url is not None:
            result['gifDynamicUrl'] = self.gif_dynamic_url
        if self.gif_static_url is not None:
            result['gifStaticUrl'] = self.gif_static_url
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.initiator is not None:
            result['initiator'] = self.initiator
        if self.interaction_type is not None:
            result['interactionType'] = self.interaction_type
        if self.introduce is not None:
            result['introduce'] = self.introduce
        if self.name is not None:
            result['name'] = self.name
        if self.opening_remarks is not None:
            result['openingRemarks'] = self.opening_remarks
        if self.order_ack_flag is not None:
            result['orderAckFlag'] = self.order_ack_flag
        result['sampleDialogueList'] = []
        if self.sample_dialogue_list is not None:
            for k in self.sample_dialogue_list:
                result['sampleDialogueList'].append(k.to_map() if k else None)
        if self.score_config is not None:
            result['scoreConfig'] = self.score_config.to_map()
        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id
        if self.sparring_tip_content is not None:
            result['sparringTipContent'] = self.sparring_tip_content
        if self.sparring_tip_title is not None:
            result['sparringTipTitle'] = self.sparring_tip_title
        if self.status is not None:
            result['status'] = self.status
        if self.student_think_time_flag is not None:
            result['studentThinkTimeFlag'] = self.student_think_time_flag
        if self.type is not None:
            result['type'] = self.type
        if self.weights is not None:
            result['weights'] = self.weights.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendQuestionFlag') is not None:
            self.append_question_flag = m.get('appendQuestionFlag')
        if m.get('assessmentScope') is not None:
            self.assessment_scope = m.get('assessmentScope')
        if m.get('closingRemarks') is not None:
            self.closing_remarks = m.get('closingRemarks')
        if m.get('completeStrategy') is not None:
            temp_model = ListAICoachScriptPageResponseBodyListCompleteStrategy()
            self.complete_strategy = temp_model.from_map(m['completeStrategy'])
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')
        if m.get('dialogueTextFlag') is not None:
            self.dialogue_text_flag = m.get('dialogueTextFlag')
        if m.get('dialogueTipFlag') is not None:
            self.dialogue_tip_flag = m.get('dialogueTipFlag')
        if m.get('evaluateReportFlag') is not None:
            self.evaluate_report_flag = m.get('evaluateReportFlag')
        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')
        if m.get('gifDynamicUrl') is not None:
            self.gif_dynamic_url = m.get('gifDynamicUrl')
        if m.get('gifStaticUrl') is not None:
            self.gif_static_url = m.get('gifStaticUrl')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')
        if m.get('interactionType') is not None:
            self.interaction_type = m.get('interactionType')
        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('openingRemarks') is not None:
            self.opening_remarks = m.get('openingRemarks')
        if m.get('orderAckFlag') is not None:
            self.order_ack_flag = m.get('orderAckFlag')
        self.sample_dialogue_list = []
        if m.get('sampleDialogueList') is not None:
            for k in m.get('sampleDialogueList'):
                temp_model = ListAICoachScriptPageResponseBodyListSampleDialogueList()
                self.sample_dialogue_list.append(temp_model.from_map(k))
        if m.get('scoreConfig') is not None:
            temp_model = ListAICoachScriptPageResponseBodyListScoreConfig()
            self.score_config = temp_model.from_map(m['scoreConfig'])
        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')
        if m.get('sparringTipContent') is not None:
            self.sparring_tip_content = m.get('sparringTipContent')
        if m.get('sparringTipTitle') is not None:
            self.sparring_tip_title = m.get('sparringTipTitle')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('studentThinkTimeFlag') is not None:
            self.student_think_time_flag = m.get('studentThinkTimeFlag')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('weights') is not None:
            temp_model = ListAICoachScriptPageResponseBodyListWeights()
            self.weights = temp_model.from_map(m['weights'])
        return self


class ListAICoachScriptPageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        list: List[ListAICoachScriptPageResponseBodyList] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
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
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListAICoachScriptPageResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAICoachScriptPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAICoachScriptPageResponseBody = None,
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
            temp_model = ListAICoachScriptPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAICoachTaskPageRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        status: str = None,
        student_id: str = None,
        task_id: str = None,
    ):
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.status = status
        self.student_id = student_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.student_id is not None:
            result['studentId'] = self.student_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('studentId') is not None:
            self.student_id = m.get('studentId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListAICoachTaskPageResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        finish_time: str = None,
        gmt_create: str = None,
        status: str = None,
        student_id: str = None,
        task_id: str = None,
    ):
        self.finish_time = finish_time
        self.gmt_create = gmt_create
        self.status = status
        self.student_id = student_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.status is not None:
            result['status'] = self.status
        if self.student_id is not None:
            result['studentId'] = self.student_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('studentId') is not None:
            self.student_id = m.get('studentId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListAICoachTaskPageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[ListAICoachTaskPageResponseBodyTaskList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['taskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['taskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.task_list = []
        if m.get('taskList') is not None:
            for k in m.get('taskList'):
                temp_model = ListAICoachTaskPageResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListAICoachTaskPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAICoachTaskPageResponseBody = None,
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
            temp_model = ListAICoachTaskPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentsRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_scene: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        self.agent_id = agent_id
        self.agent_scene = agent_scene
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
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
        if self.agent_scene is not None:
            result['agentScene'] = self.agent_scene
        if self.owner is not None:
            result['owner'] = self.owner
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('agentScene') is not None:
            self.agent_scene = m.get('agentScene')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAgentsResponseBodyList(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        agent_scene: str = None,
        characters_description: str = None,
        enable_interaction: int = None,
        industry: str = None,
        online_search: bool = None,
        owner: str = None,
        reference_url: str = None,
        status: int = None,
        text_style: str = None,
        viewer: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_scene = agent_scene
        self.characters_description = characters_description
        self.enable_interaction = enable_interaction
        self.industry = industry
        self.online_search = online_search
        self.owner = owner
        self.reference_url = reference_url
        self.status = status
        self.text_style = text_style
        self.viewer = viewer

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
        if self.agent_scene is not None:
            result['agentScene'] = self.agent_scene
        if self.characters_description is not None:
            result['charactersDescription'] = self.characters_description
        if self.enable_interaction is not None:
            result['enableInteraction'] = self.enable_interaction
        if self.industry is not None:
            result['industry'] = self.industry
        if self.online_search is not None:
            result['onlineSearch'] = self.online_search
        if self.owner is not None:
            result['owner'] = self.owner
        if self.reference_url is not None:
            result['referenceUrl'] = self.reference_url
        if self.status is not None:
            result['status'] = self.status
        if self.text_style is not None:
            result['textStyle'] = self.text_style
        if self.viewer is not None:
            result['viewer'] = self.viewer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')
        if m.get('agentScene') is not None:
            self.agent_scene = m.get('agentScene')
        if m.get('charactersDescription') is not None:
            self.characters_description = m.get('charactersDescription')
        if m.get('enableInteraction') is not None:
            self.enable_interaction = m.get('enableInteraction')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('onlineSearch') is not None:
            self.online_search = m.get('onlineSearch')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('referenceUrl') is not None:
            self.reference_url = m.get('referenceUrl')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('textStyle') is not None:
            self.text_style = m.get('textStyle')
        if m.get('viewer') is not None:
            self.viewer = m.get('viewer')
        return self


class ListAgentsResponseBody(TeaModel):
    def __init__(
        self,
        list: List[ListAgentsResponseBodyList] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.list = list
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
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListAgentsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAgentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentsResponseBody = None,
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
            temp_model = ListAgentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnchorRequest(TeaModel):
    def __init__(
        self,
        anchor_category: str = None,
        anchor_id: str = None,
        anchor_type: str = None,
        cover_rate: str = None,
        digital_human_type: str = None,
        page_number: int = None,
        page_size: int = None,
        res_spec_type: str = None,
        use_scene: str = None,
    ):
        self.anchor_category = anchor_category
        self.anchor_id = anchor_id
        self.anchor_type = anchor_type
        self.cover_rate = cover_rate
        self.digital_human_type = digital_human_type
        self.page_number = page_number
        self.page_size = page_size
        self.res_spec_type = res_spec_type
        self.use_scene = use_scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_category is not None:
            result['anchorCategory'] = self.anchor_category
        if self.anchor_id is not None:
            result['anchorId'] = self.anchor_id
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
        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorCategory') is not None:
            self.anchor_category = m.get('anchorCategory')
        if m.get('anchorId') is not None:
            self.anchor_id = m.get('anchorId')
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
        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')
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


class ListAvatarProjectRequest(TeaModel):
    def __init__(
        self,
        project_id_list: List[str] = None,
    ):
        self.project_id_list = project_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id_list is not None:
            result['projectIdList'] = self.project_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectIdList') is not None:
            self.project_id_list = m.get('projectIdList')
        return self


class ListAvatarProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        project_id_list_shrink: str = None,
    ):
        self.project_id_list_shrink = project_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id_list_shrink is not None:
            result['projectIdList'] = self.project_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectIdList') is not None:
            self.project_id_list_shrink = m.get('projectIdList')
        return self


class ListAvatarProjectResponseBodyQueryAvatarProjectResultList(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        error_msg: str = None,
        project_id: str = None,
        project_name: str = None,
        status: str = None,
    ):
        self.agent_id = agent_id
        self.error_msg = error_msg
        self.project_id = project_id
        self.project_name = project_name
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
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAvatarProjectResponseBody(TeaModel):
    def __init__(
        self,
        query_avatar_project_result_list: List[ListAvatarProjectResponseBodyQueryAvatarProjectResultList] = None,
        request_id: str = None,
    ):
        self.query_avatar_project_result_list = query_avatar_project_result_list
        self.request_id = request_id

    def validate(self):
        if self.query_avatar_project_result_list:
            for k in self.query_avatar_project_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['queryAvatarProjectResultList'] = []
        if self.query_avatar_project_result_list is not None:
            for k in self.query_avatar_project_result_list:
                result['queryAvatarProjectResultList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_avatar_project_result_list = []
        if m.get('queryAvatarProjectResultList') is not None:
            for k in m.get('queryAvatarProjectResultList'):
                temp_model = ListAvatarProjectResponseBodyQueryAvatarProjectResultList()
                self.query_avatar_project_result_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListAvatarProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvatarProjectResponseBody = None,
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
            temp_model = ListAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKnowledgeBaseRequest(TeaModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.knowledge_base_id = knowledge_base_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListKnowledgeBaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KnowledgeBaseListResult = None,
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
            temp_model = KnowledgeBaseListResult()
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
        res_spec_type: str = None,
        use_scene: str = None,
        voice_language: str = None,
        voice_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.res_spec_type = res_spec_type
        self.use_scene = use_scene
        self.voice_language = voice_language
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
        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type
        if self.use_scene is not None:
            result['useScene'] = self.use_scene
        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language
        if self.voice_type is not None:
            result['voiceType'] = self.voice_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')
        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')
        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')
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


class OperateAvatarProjectRequest(TeaModel):
    def __init__(
        self,
        operate_type: str = None,
        project_id: str = None,
        res_channel_number: int = None,
        res_type: str = None,
    ):
        self.operate_type = operate_type
        self.project_id = project_id
        self.res_channel_number = res_channel_number
        self.res_type = res_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_type is not None:
            result['operateType'] = self.operate_type
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.res_channel_number is not None:
            result['resChannelNumber'] = self.res_channel_number
        if self.res_type is not None:
            result['resType'] = self.res_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('resChannelNumber') is not None:
            self.res_channel_number = m.get('resChannelNumber')
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        return self


class OperateAvatarProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # Id of the request
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


class OperateAvatarProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateAvatarProjectResponseBody = None,
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
            temp_model = OperateAvatarProjectResponseBody()
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


class QueryAvatarProjectResponseBodyFramesLayersMaterial(TeaModel):
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


class QueryAvatarProjectResponseBodyFramesLayers(TeaModel):
    def __init__(
        self,
        height: int = None,
        index: int = None,
        material: QueryAvatarProjectResponseBodyFramesLayersMaterial = None,
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
            temp_model = QueryAvatarProjectResponseBodyFramesLayersMaterial()
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


class QueryAvatarProjectResponseBodyFramesVideoScript(TeaModel):
    def __init__(
        self,
        emotion: str = None,
        pitch_rate: str = None,
        speed_rate: str = None,
        text_content: str = None,
        voice_language: str = None,
        voice_template_id: str = None,
        volume: int = None,
    ):
        self.emotion = emotion
        self.pitch_rate = pitch_rate
        self.speed_rate = speed_rate
        self.text_content = text_content
        self.voice_language = voice_language
        self.voice_template_id = voice_template_id
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion is not None:
            result['emotion'] = self.emotion
        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate
        if self.speed_rate is not None:
            result['speedRate'] = self.speed_rate
        if self.text_content is not None:
            result['textContent'] = self.text_content
        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language
        if self.voice_template_id is not None:
            result['voiceTemplateId'] = self.voice_template_id
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('emotion') is not None:
            self.emotion = m.get('emotion')
        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')
        if m.get('speedRate') is not None:
            self.speed_rate = m.get('speedRate')
        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')
        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')
        if m.get('voiceTemplateId') is not None:
            self.voice_template_id = m.get('voiceTemplateId')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        return self


class QueryAvatarProjectResponseBodyFrames(TeaModel):
    def __init__(
        self,
        index: int = None,
        layers: List[QueryAvatarProjectResponseBodyFramesLayers] = None,
        video_script: QueryAvatarProjectResponseBodyFramesVideoScript = None,
    ):
        self.index = index
        self.layers = layers
        self.video_script = video_script

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
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
                temp_model = QueryAvatarProjectResponseBodyFramesLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('videoScript') is not None:
            temp_model = QueryAvatarProjectResponseBodyFramesVideoScript()
            self.video_script = temp_model.from_map(m['videoScript'])
        return self


class QueryAvatarProjectResponseBody(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        error_msg: str = None,
        frames: List[QueryAvatarProjectResponseBodyFrames] = None,
        project_name: str = None,
        request_id: str = None,
        res_spec_type: str = None,
        scale_type: str = None,
        script_model_tag: str = None,
        status: str = None,
    ):
        self.agent_id = agent_id
        self.error_msg = error_msg
        self.frames = frames
        self.project_name = project_name
        self.request_id = request_id
        self.res_spec_type = res_spec_type
        self.scale_type = scale_type
        self.script_model_tag = script_model_tag
        self.status = status

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
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        result['frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['frames'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type
        if self.scale_type is not None:
            result['scaleType'] = self.scale_type
        if self.script_model_tag is not None:
            result['scriptModelTag'] = self.script_model_tag
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        self.frames = []
        if m.get('frames') is not None:
            for k in m.get('frames'):
                temp_model = QueryAvatarProjectResponseBodyFrames()
                self.frames.append(temp_model.from_map(k))
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')
        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')
        if m.get('scriptModelTag') is not None:
            self.script_model_tag = m.get('scriptModelTag')
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


class QueryImageToVideoTaskRequest(TeaModel):
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


class QueryImageToVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        origin_url: str = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.message = message
        self.origin_url = origin_url
        self.request_id = request_id
        self.status = status
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.origin_url is not None:
            result['originUrl'] = self.origin_url
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('originUrl') is not None:
            self.origin_url = m.get('originUrl')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class QueryImageToVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryImageToVideoTaskResponseBody = None,
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
            temp_model = QueryImageToVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIndividuationTextTaskRequest(TeaModel):
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


class QueryIndividuationTextTaskResponseBodyTextList(TeaModel):
    def __init__(
        self,
        status: int = None,
        text_id: str = None,
        user_id: str = None,
    ):
        self.status = status
        self.text_id = text_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.text_id is not None:
            result['textId'] = self.text_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('textId') is not None:
            self.text_id = m.get('textId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryIndividuationTextTaskResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        request_id: str = None,
        status: int = None,
        text_list: List[QueryIndividuationTextTaskResponseBodyTextList] = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.text_list = text_list
        self.update_time = update_time

    def validate(self):
        if self.text_list:
            for k in self.text_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        result['textList'] = []
        if self.text_list is not None:
            for k in self.text_list:
                result['textList'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.text_list = []
        if m.get('textList') is not None:
            for k in m.get('textList'):
                temp_model = QueryIndividuationTextTaskResponseBodyTextList()
                self.text_list.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class QueryIndividuationTextTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIndividuationTextTaskResponseBody = None,
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
            temp_model = QueryIndividuationTextTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySessionInfoRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        project_id: str = None,
        status_list: List[str] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status_list is not None:
            result['statusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        return self


class QuerySessionInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        project_id: str = None,
        status_list_shrink: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id
        self.status_list_shrink = status_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status_list_shrink is not None:
            result['statusList'] = self.status_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('statusList') is not None:
            self.status_list_shrink = m.get('statusList')
        return self


class QuerySessionInfoResponseBodyQueryResourceInfoList(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        status: str = None,
    ):
        self.session_id = session_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QuerySessionInfoResponseBody(TeaModel):
    def __init__(
        self,
        query_resource_info_list: List[QuerySessionInfoResponseBodyQueryResourceInfoList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.query_resource_info_list = query_resource_info_list
        self.request_id = request_id
        self.total = total

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
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_resource_info_list = []
        if m.get('queryResourceInfoList') is not None:
            for k in m.get('queryResourceInfoList'):
                temp_model = QuerySessionInfoResponseBodyQueryResourceInfoList()
                self.query_resource_info_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QuerySessionInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySessionInfoResponseBody = None,
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
            temp_model = QuerySessionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTextStreamResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        index: int = None,
        message: str = None,
        type: int = None,
    ):
        self.end = end
        self.index = index
        # Id of the request
        self.message = message
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.index is not None:
            result['index'] = self.index
        if self.message is not None:
            result['message'] = self.message
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryTextStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTextStreamResponseBody = None,
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
            temp_model = QueryTextStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAvatarProjectRequestFramesLayersMaterial(TeaModel):
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


class SaveAvatarProjectRequestFramesLayers(TeaModel):
    def __init__(
        self,
        height: int = None,
        index: int = None,
        material: SaveAvatarProjectRequestFramesLayersMaterial = None,
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
            temp_model = SaveAvatarProjectRequestFramesLayersMaterial()
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


class SaveAvatarProjectRequestFramesVideoScript(TeaModel):
    def __init__(
        self,
        emotion: str = None,
        pitch_rate: str = None,
        speed_rate: str = None,
        text_content: str = None,
        voice_language: str = None,
        voice_template_id: str = None,
        volume: str = None,
    ):
        self.emotion = emotion
        self.pitch_rate = pitch_rate
        self.speed_rate = speed_rate
        self.text_content = text_content
        self.voice_language = voice_language
        self.voice_template_id = voice_template_id
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion is not None:
            result['emotion'] = self.emotion
        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate
        if self.speed_rate is not None:
            result['speedRate'] = self.speed_rate
        if self.text_content is not None:
            result['textContent'] = self.text_content
        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language
        if self.voice_template_id is not None:
            result['voiceTemplateId'] = self.voice_template_id
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('emotion') is not None:
            self.emotion = m.get('emotion')
        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')
        if m.get('speedRate') is not None:
            self.speed_rate = m.get('speedRate')
        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')
        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')
        if m.get('voiceTemplateId') is not None:
            self.voice_template_id = m.get('voiceTemplateId')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        return self


class SaveAvatarProjectRequestFrames(TeaModel):
    def __init__(
        self,
        index: int = None,
        layers: List[SaveAvatarProjectRequestFramesLayers] = None,
        video_script: SaveAvatarProjectRequestFramesVideoScript = None,
    ):
        self.index = index
        self.layers = layers
        self.video_script = video_script

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
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
                temp_model = SaveAvatarProjectRequestFramesLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('videoScript') is not None:
            temp_model = SaveAvatarProjectRequestFramesVideoScript()
            self.video_script = temp_model.from_map(m['videoScript'])
        return self


class SaveAvatarProjectRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        bit_rate: str = None,
        frame_rate: str = None,
        frames: List[SaveAvatarProjectRequestFrames] = None,
        operate_type: str = None,
        project_id: str = None,
        project_name: str = None,
        res_spec_type: str = None,
        resolution: str = None,
        scale_type: str = None,
        script_model_tag: str = None,
        synchronized_display: str = None,
    ):
        self.agent_id = agent_id
        self.bit_rate = bit_rate
        self.frame_rate = frame_rate
        self.frames = frames
        self.operate_type = operate_type
        self.project_id = project_id
        self.project_name = project_name
        self.res_spec_type = res_spec_type
        self.resolution = resolution
        self.scale_type = scale_type
        self.script_model_tag = script_model_tag
        self.synchronized_display = synchronized_display

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
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.bit_rate is not None:
            result['bitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['frameRate'] = self.frame_rate
        result['frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['frames'].append(k.to_map() if k else None)
        if self.operate_type is not None:
            result['operateType'] = self.operate_type
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.scale_type is not None:
            result['scaleType'] = self.scale_type
        if self.script_model_tag is not None:
            result['scriptModelTag'] = self.script_model_tag
        if self.synchronized_display is not None:
            result['synchronizedDisplay'] = self.synchronized_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('bitRate') is not None:
            self.bit_rate = m.get('bitRate')
        if m.get('frameRate') is not None:
            self.frame_rate = m.get('frameRate')
        self.frames = []
        if m.get('frames') is not None:
            for k in m.get('frames'):
                temp_model = SaveAvatarProjectRequestFrames()
                self.frames.append(temp_model.from_map(k))
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')
        if m.get('scriptModelTag') is not None:
            self.script_model_tag = m.get('scriptModelTag')
        if m.get('synchronizedDisplay') is not None:
            self.synchronized_display = m.get('synchronizedDisplay')
        return self


class SaveAvatarProjectResponseBody(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        error_code: str = None,
        error_message: str = None,
        error_msg: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.agent_id = agent_id
        self.error_code = error_code
        self.error_message = error_message
        self.error_msg = error_msg
        self.project_id = project_id
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
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.project_id is not None:
            result['projectId'] = self.project_id
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
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SaveAvatarProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveAvatarProjectResponseBody = None,
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
            temp_model = SaveAvatarProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectImageTaskResponseBodyImageInfos(TeaModel):
    def __init__(
        self,
        custom_image_url: str = None,
        gmt_create: str = None,
        image_h: str = None,
        image_w: str = None,
    ):
        self.custom_image_url = custom_image_url
        self.gmt_create = gmt_create
        self.image_h = image_h
        self.image_w = image_w

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_image_url is not None:
            result['customImageUrl'] = self.custom_image_url
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.image_h is not None:
            result['imageH'] = self.image_h
        if self.image_w is not None:
            result['imageW'] = self.image_w
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customImageUrl') is not None:
            self.custom_image_url = m.get('customImageUrl')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('imageH') is not None:
            self.image_h = m.get('imageH')
        if m.get('imageW') is not None:
            self.image_w = m.get('imageW')
        return self


class SelectImageTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        failed: str = None,
        generation_source: str = None,
        gmt_create: str = None,
        image_infos: List[SelectImageTaskResponseBodyImageInfos] = None,
        request_id: str = None,
        scene: str = None,
        status: str = None,
        subtask_processing: str = None,
        success: str = None,
        total: str = None,
    ):
        self.error_message = error_message
        self.failed = failed
        self.generation_source = generation_source
        self.gmt_create = gmt_create
        self.image_infos = image_infos
        # Id of the request
        self.request_id = request_id
        self.scene = scene
        self.status = status
        self.subtask_processing = subtask_processing
        self.success = success
        self.total = total

    def validate(self):
        if self.image_infos:
            for k in self.image_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.failed is not None:
            result['failed'] = self.failed
        if self.generation_source is not None:
            result['generationSource'] = self.generation_source
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        result['imageInfos'] = []
        if self.image_infos is not None:
            for k in self.image_infos:
                result['imageInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.scene is not None:
            result['scene'] = self.scene
        if self.status is not None:
            result['status'] = self.status
        if self.subtask_processing is not None:
            result['subtaskProcessing'] = self.subtask_processing
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('generationSource') is not None:
            self.generation_source = m.get('generationSource')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        self.image_infos = []
        if m.get('imageInfos') is not None:
            for k in m.get('imageInfos'):
                temp_model = SelectImageTaskResponseBodyImageInfos()
                self.image_infos.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subtaskProcessing') is not None:
            self.subtask_processing = m.get('subtaskProcessing')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class SelectImageTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectImageTaskResponseBody = None,
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
            temp_model = SelectImageTaskResponseBody()
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
        aliyun_uid: str = None,
        request_id: str = None,
        resource_info_list: List[SelectResourceResponseBodyResourceInfoList] = None,
    ):
        self.aliyun_uid = aliyun_uid
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
        if self.aliyun_uid is not None:
            result['aliyunUid'] = self.aliyun_uid
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceInfoList'] = []
        if self.resource_info_list is not None:
            for k in self.resource_info_list:
                result['resourceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunUid') is not None:
            self.aliyun_uid = m.get('aliyunUid')
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


class SendSdkMessageRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        header: str = None,
        module_name: str = None,
        operation_name: str = None,
        user_id: str = None,
    ):
        self.data = data
        self.header = header
        self.module_name = module_name
        self.operation_name = operation_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.header is not None:
            result['header'] = self.header
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.operation_name is not None:
            result['operationName'] = self.operation_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('header') is not None:
            self.header = m.get('header')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('operationName') is not None:
            self.operation_name = m.get('operationName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SendSdkMessageResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # true
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SendSdkMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendSdkMessageResponseBody = None,
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
            temp_model = SendSdkMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendSdkStreamMessageRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        header: str = None,
        module_name: str = None,
        operation_name: str = None,
        user_id: str = None,
    ):
        self.data = data
        # header
        self.header = header
        self.module_name = module_name
        self.operation_name = operation_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.header is not None:
            result['header'] = self.header
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.operation_name is not None:
            result['operationName'] = self.operation_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('header') is not None:
            self.header = m.get('header')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('operationName') is not None:
            self.operation_name = m.get('operationName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SendSdkStreamMessageResponseBody(TeaModel):
    def __init__(
        self,
        common_stream_message: str = None,
    ):
        self.common_stream_message = common_stream_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_stream_message is not None:
            result['commonStreamMessage'] = self.common_stream_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonStreamMessage') is not None:
            self.common_stream_message = m.get('commonStreamMessage')
        return self


class SendSdkStreamMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendSdkStreamMessageResponseBody = None,
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
            temp_model = SendSdkStreamMessageResponseBody()
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
        channel_token: str = None,
        custom_push_url: str = None,
        custom_user_id: str = None,
        project_id: str = None,
        request_id: str = None,
    ):
        self.channel_token = channel_token
        self.custom_push_url = custom_push_url
        self.custom_user_id = custom_user_id
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_token is not None:
            result['channelToken'] = self.channel_token
        if self.custom_push_url is not None:
            result['customPushUrl'] = self.custom_push_url
        if self.custom_user_id is not None:
            result['customUserId'] = self.custom_user_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToken') is not None:
            self.channel_token = m.get('channelToken')
        if m.get('customPushUrl') is not None:
            self.custom_push_url = m.get('customPushUrl')
        if m.get('customUserId') is not None:
            self.custom_user_id = m.get('customUserId')
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
        token: str = None,
        web_socket_url: str = None,
    ):
        self.channel_token = channel_token
        self.request_id = request_id
        self.session_id = session_id
        self.token = token
        self.web_socket_url = web_socket_url

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
        if self.token is not None:
            result['token'] = self.token
        if self.web_socket_url is not None:
            result['webSocketUrl'] = self.web_socket_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToken') is not None:
            self.channel_token = m.get('channelToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('webSocketUrl') is not None:
            self.web_socket_url = m.get('webSocketUrl')
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


class SubmitImageToVideoTaskRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        pos_prompt: str = None,
    ):
        self.image_url = image_url
        self.pos_prompt = pos_prompt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.pos_prompt is not None:
            result['posPrompt'] = self.pos_prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('posPrompt') is not None:
            self.pos_prompt = m.get('posPrompt')
        return self


class SubmitImageToVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitImageToVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitImageToVideoTaskResponseBody = None,
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
            temp_model = SubmitImageToVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitProjectTaskRequestFramesLayersMaterialMask(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class SubmitProjectTaskRequestFramesLayersMaterial(TeaModel):
    def __init__(
        self,
        anchor_style_level: str = None,
        format: str = None,
        id: str = None,
        mask: SubmitProjectTaskRequestFramesLayersMaterialMask = None,
        speed: str = None,
        url: str = None,
        volume: int = None,
    ):
        self.anchor_style_level = anchor_style_level
        self.format = format
        self.id = id
        self.mask = mask
        self.speed = speed
        self.url = url
        self.volume = volume

    def validate(self):
        if self.mask:
            self.mask.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_style_level is not None:
            result['anchorStyleLevel'] = self.anchor_style_level
        if self.format is not None:
            result['format'] = self.format
        if self.id is not None:
            result['id'] = self.id
        if self.mask is not None:
            result['mask'] = self.mask.to_map()
        if self.speed is not None:
            result['speed'] = self.speed
        if self.url is not None:
            result['url'] = self.url
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorStyleLevel') is not None:
            self.anchor_style_level = m.get('anchorStyleLevel')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mask') is not None:
            temp_model = SubmitProjectTaskRequestFramesLayersMaterialMask()
            self.mask = temp_model.from_map(m['mask'])
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
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
        emotion: str = None,
        pitch_rate: str = None,
        speech_open: bool = None,
        speed_rate: str = None,
        text_content: str = None,
        type: str = None,
        voice_language: str = None,
        voice_template_id: int = None,
        volume: int = None,
    ):
        self.audio_url = audio_url
        self.emotion = emotion
        self.pitch_rate = pitch_rate
        self.speech_open = speech_open
        self.speed_rate = speed_rate
        self.text_content = text_content
        self.type = type
        self.voice_language = voice_language
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
        if self.emotion is not None:
            result['emotion'] = self.emotion
        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate
        if self.speech_open is not None:
            result['speechOpen'] = self.speech_open
        if self.speed_rate is not None:
            result['speedRate'] = self.speed_rate
        if self.text_content is not None:
            result['textContent'] = self.text_content
        if self.type is not None:
            result['type'] = self.type
        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language
        if self.voice_template_id is not None:
            result['voiceTemplateId'] = self.voice_template_id
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioUrl') is not None:
            self.audio_url = m.get('audioUrl')
        if m.get('emotion') is not None:
            self.emotion = m.get('emotion')
        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')
        if m.get('speechOpen') is not None:
            self.speech_open = m.get('speechOpen')
        if m.get('speedRate') is not None:
            self.speed_rate = m.get('speedRate')
        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')
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


class TransferPortraitStyleRequest(TeaModel):
    def __init__(
        self,
        height: int = None,
        image_url: str = None,
        numbers: int = None,
        redraw_amplitude: int = None,
        style: int = None,
        width: int = None,
    ):
        self.height = height
        self.image_url = image_url
        self.numbers = numbers
        self.redraw_amplitude = redraw_amplitude
        self.style = style
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.numbers is not None:
            result['numbers'] = self.numbers
        if self.redraw_amplitude is not None:
            result['redrawAmplitude'] = self.redraw_amplitude
        if self.style is not None:
            result['style'] = self.style
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('numbers') is not None:
            self.numbers = m.get('numbers')
        if m.get('redrawAmplitude') is not None:
            self.redraw_amplitude = m.get('redrawAmplitude')
        if m.get('style') is not None:
            self.style = m.get('style')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class TransferPortraitStyleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
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


class TransferPortraitStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferPortraitStyleResponseBody = None,
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
            temp_model = TransferPortraitStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


