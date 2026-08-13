# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListUserVisibleKnowledgeBaseContentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListUserVisibleKnowledgeBaseContentsResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        self.items = items
        # 错误描述，成功时为空
        self.message = message
        # 当前页码
        self.page = page
        # 每页数量
        self.page_size = page_size
        # 请求追踪 ID
        self.request_id = request_id
        # 命中总数
        self.total_count = total_count

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
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListUserVisibleKnowledgeBaseContentsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListUserVisibleKnowledgeBaseContentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        description: str = None,
        directory_kind: str = None,
        directory_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        item_id: str = None,
        item_type: str = None,
        kb_submission_pending: bool = None,
        modifier_name: str = None,
        name: str = None,
        object_bindings: List[Dict[str, Any]] = None,
        oo_visibility_mode: str = None,
        read_only: bool = None,
        share_infos: List[main_models.ListUserVisibleKnowledgeBaseContentsResponseBodyItemsShareInfos] = None,
        shared: bool = None,
        source_failed_count: int = None,
        source_kind: str = None,
        source_ready_count: int = None,
        source_status: str = None,
        source_total_count: int = None,
        source_type: str = None,
    ):
        # 创建人名称
        self.creator_name = creator_name
        # 知识库描述
        self.description = description
        # 目录归属类型
        self.directory_kind = directory_kind
        # 目录类型
        self.directory_type = directory_type
        # 创建时间戳（毫秒）
        self.gmt_create = gmt_create
        # 修改时间戳（毫秒）
        self.gmt_modified = gmt_modified
        # 目录 ID 或资源 ID
        self.item_id = item_id
        # 内容类型：directory 或 resource
        self.item_type = item_type
        # 资源是否存在待审批的知识库提交记录
        self.kb_submission_pending = kb_submission_pending
        # 更新人名称
        self.modifier_name = modifier_name
        # 目录或资源名称
        self.name = name
        self.object_bindings = object_bindings
        # 知识库对数字员工的可见模式
        self.oo_visibility_mode = oo_visibility_mode
        # 是否为只读关联内容
        self.read_only = read_only
        self.share_infos = share_infos
        # 是否已直接共享到企业知识库
        self.shared = shared
        # 目录 FAILED 资源数
        self.source_failed_count = source_failed_count
        # 资源归属类型
        self.source_kind = source_kind
        # 目录 READY 资源数
        self.source_ready_count = source_ready_count
        # 资源状态；本接口只返回 READY 资源
        self.source_status = source_status
        # 目录资源总数
        self.source_total_count = source_total_count
        # 资源类型，目录项为空
        self.source_type = source_type

    def validate(self):
        if self.share_infos:
            for v1 in self.share_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.description is not None:
            result['description'] = self.description

        if self.directory_kind is not None:
            result['directoryKind'] = self.directory_kind

        if self.directory_type is not None:
            result['directoryType'] = self.directory_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.kb_submission_pending is not None:
            result['kbSubmissionPending'] = self.kb_submission_pending

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        if self.object_bindings is not None:
            result['objectBindings'] = self.object_bindings

        if self.oo_visibility_mode is not None:
            result['ooVisibilityMode'] = self.oo_visibility_mode

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        result['shareInfos'] = []
        if self.share_infos is not None:
            for k1 in self.share_infos:
                result['shareInfos'].append(k1.to_map() if k1 else None)

        if self.shared is not None:
            result['shared'] = self.shared

        if self.source_failed_count is not None:
            result['sourceFailedCount'] = self.source_failed_count

        if self.source_kind is not None:
            result['sourceKind'] = self.source_kind

        if self.source_ready_count is not None:
            result['sourceReadyCount'] = self.source_ready_count

        if self.source_status is not None:
            result['sourceStatus'] = self.source_status

        if self.source_total_count is not None:
            result['sourceTotalCount'] = self.source_total_count

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryKind') is not None:
            self.directory_kind = m.get('directoryKind')

        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('kbSubmissionPending') is not None:
            self.kb_submission_pending = m.get('kbSubmissionPending')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectBindings') is not None:
            self.object_bindings = m.get('objectBindings')

        if m.get('ooVisibilityMode') is not None:
            self.oo_visibility_mode = m.get('ooVisibilityMode')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        self.share_infos = []
        if m.get('shareInfos') is not None:
            for k1 in m.get('shareInfos'):
                temp_model = main_models.ListUserVisibleKnowledgeBaseContentsResponseBodyItemsShareInfos()
                self.share_infos.append(temp_model.from_map(k1))

        if m.get('shared') is not None:
            self.shared = m.get('shared')

        if m.get('sourceFailedCount') is not None:
            self.source_failed_count = m.get('sourceFailedCount')

        if m.get('sourceKind') is not None:
            self.source_kind = m.get('sourceKind')

        if m.get('sourceReadyCount') is not None:
            self.source_ready_count = m.get('sourceReadyCount')

        if m.get('sourceStatus') is not None:
            self.source_status = m.get('sourceStatus')

        if m.get('sourceTotalCount') is not None:
            self.source_total_count = m.get('sourceTotalCount')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

class ListUserVisibleKnowledgeBaseContentsResponseBodyItemsShareInfos(DaraModel):
    def __init__(
        self,
        submission_id: str = None,
        submitter_id: int = None,
        submitter_name: str = None,
        target_directory_id: str = None,
        target_directory_name: str = None,
        target_kb_root_directory_id: str = None,
        target_kb_root_directory_name: str = None,
    ):
        # 知识库提交审批单 ID
        self.submission_id = submission_id
        # 提交人用户 ID
        self.submitter_id = submitter_id
        # 提交人名称
        self.submitter_name = submitter_name
        # 目标目录 ID
        self.target_directory_id = target_directory_id
        # 目标目录名称
        self.target_directory_name = target_directory_name
        # 目标企业知识库根目录 ID
        self.target_kb_root_directory_id = target_kb_root_directory_id
        # 目标企业知识库名称
        self.target_kb_root_directory_name = target_kb_root_directory_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.submission_id is not None:
            result['submissionId'] = self.submission_id

        if self.submitter_id is not None:
            result['submitterId'] = self.submitter_id

        if self.submitter_name is not None:
            result['submitterName'] = self.submitter_name

        if self.target_directory_id is not None:
            result['targetDirectoryId'] = self.target_directory_id

        if self.target_directory_name is not None:
            result['targetDirectoryName'] = self.target_directory_name

        if self.target_kb_root_directory_id is not None:
            result['targetKbRootDirectoryId'] = self.target_kb_root_directory_id

        if self.target_kb_root_directory_name is not None:
            result['targetKbRootDirectoryName'] = self.target_kb_root_directory_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('submissionId') is not None:
            self.submission_id = m.get('submissionId')

        if m.get('submitterId') is not None:
            self.submitter_id = m.get('submitterId')

        if m.get('submitterName') is not None:
            self.submitter_name = m.get('submitterName')

        if m.get('targetDirectoryId') is not None:
            self.target_directory_id = m.get('targetDirectoryId')

        if m.get('targetDirectoryName') is not None:
            self.target_directory_name = m.get('targetDirectoryName')

        if m.get('targetKbRootDirectoryId') is not None:
            self.target_kb_root_directory_id = m.get('targetKbRootDirectoryId')

        if m.get('targetKbRootDirectoryName') is not None:
            self.target_kb_root_directory_name = m.get('targetKbRootDirectoryName')

        return self

