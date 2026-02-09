# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class GetGameReviewByStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.GetGameReviewByStatusResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.GetGameReviewByStatusResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class GetGameReviewByStatusResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        content: List[main_models.GetGameReviewByStatusResponseBodyResultContentContent] = None,
        error_code: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.content = content
        self.error_code = error_code
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.GetGameReviewByStatusResponseBodyResultContentContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetGameReviewByStatusResponseBodyResultContentContent(DaraModel):
    def __init__(
        self,
        appendix: str = None,
        auto_online: bool = None,
        creator: str = None,
        extension: str = None,
        flow_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icons: List[str] = None,
        id: int = None,
        review_channel: str = None,
        review_integer_status: int = None,
        review_progress: List[main_models.GetGameReviewByStatusResponseBodyResultContentContentReviewProgress] = None,
        review_status: str = None,
        review_target: int = None,
        target_detail: main_models.GetGameReviewByStatusResponseBodyResultContentContentTargetDetail = None,
        target_type: str = None,
    ):
        self.appendix = appendix
        self.auto_online = auto_online
        self.creator = creator
        self.extension = extension
        self.flow_id = flow_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icons = icons
        self.id = id
        self.review_channel = review_channel
        self.review_integer_status = review_integer_status
        self.review_progress = review_progress
        self.review_status = review_status
        self.review_target = review_target
        self.target_detail = target_detail
        self.target_type = target_type

    def validate(self):
        if self.review_progress:
            for v1 in self.review_progress:
                 if v1:
                    v1.validate()
        if self.target_detail:
            self.target_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appendix is not None:
            result['Appendix'] = self.appendix

        if self.auto_online is not None:
            result['AutoOnline'] = self.auto_online

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icons is not None:
            result['Icons'] = self.icons

        if self.id is not None:
            result['Id'] = self.id

        if self.review_channel is not None:
            result['ReviewChannel'] = self.review_channel

        if self.review_integer_status is not None:
            result['ReviewIntegerStatus'] = self.review_integer_status

        result['ReviewProgress'] = []
        if self.review_progress is not None:
            for k1 in self.review_progress:
                result['ReviewProgress'].append(k1.to_map() if k1 else None)

        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status

        if self.review_target is not None:
            result['ReviewTarget'] = self.review_target

        if self.target_detail is not None:
            result['TargetDetail'] = self.target_detail.to_map()

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Appendix') is not None:
            self.appendix = m.get('Appendix')

        if m.get('AutoOnline') is not None:
            self.auto_online = m.get('AutoOnline')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Icons') is not None:
            self.icons = m.get('Icons')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ReviewChannel') is not None:
            self.review_channel = m.get('ReviewChannel')

        if m.get('ReviewIntegerStatus') is not None:
            self.review_integer_status = m.get('ReviewIntegerStatus')

        self.review_progress = []
        if m.get('ReviewProgress') is not None:
            for k1 in m.get('ReviewProgress'):
                temp_model = main_models.GetGameReviewByStatusResponseBodyResultContentContentReviewProgress()
                self.review_progress.append(temp_model.from_map(k1))

        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')

        if m.get('ReviewTarget') is not None:
            self.review_target = m.get('ReviewTarget')

        if m.get('TargetDetail') is not None:
            temp_model = main_models.GetGameReviewByStatusResponseBodyResultContentContentTargetDetail()
            self.target_detail = temp_model.from_map(m.get('TargetDetail'))

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class GetGameReviewByStatusResponseBodyResultContentContentTargetDetail(DaraModel):
    def __init__(
        self,
        auto_online: bool = None,
        category: str = None,
        detail: str = None,
        game_maker: str = None,
        icon_url: str = None,
        introduction: str = None,
        mini_program_code: str = None,
        mini_program_info_id: int = None,
        mini_program_name: str = None,
        mini_resource_id: int = None,
        publish_status: int = None,
        qr_code_url: str = None,
        review_target_type: str = None,
        sub_type: int = None,
        target_id: int = None,
        version: str = None,
    ):
        self.auto_online = auto_online
        self.category = category
        self.detail = detail
        self.game_maker = game_maker
        self.icon_url = icon_url
        self.introduction = introduction
        self.mini_program_code = mini_program_code
        self.mini_program_info_id = mini_program_info_id
        self.mini_program_name = mini_program_name
        self.mini_resource_id = mini_resource_id
        self.publish_status = publish_status
        self.qr_code_url = qr_code_url
        self.review_target_type = review_target_type
        self.sub_type = sub_type
        self.target_id = target_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_online is not None:
            result['AutoOnline'] = self.auto_online

        if self.category is not None:
            result['Category'] = self.category

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.game_maker is not None:
            result['GameMaker'] = self.game_maker

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.mini_program_code is not None:
            result['MiniProgramCode'] = self.mini_program_code

        if self.mini_program_info_id is not None:
            result['MiniProgramInfoId'] = self.mini_program_info_id

        if self.mini_program_name is not None:
            result['MiniProgramName'] = self.mini_program_name

        if self.mini_resource_id is not None:
            result['MiniResourceId'] = self.mini_resource_id

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.qr_code_url is not None:
            result['QrCodeUrl'] = self.qr_code_url

        if self.review_target_type is not None:
            result['ReviewTargetType'] = self.review_target_type

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoOnline') is not None:
            self.auto_online = m.get('AutoOnline')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('GameMaker') is not None:
            self.game_maker = m.get('GameMaker')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('MiniProgramCode') is not None:
            self.mini_program_code = m.get('MiniProgramCode')

        if m.get('MiniProgramInfoId') is not None:
            self.mini_program_info_id = m.get('MiniProgramInfoId')

        if m.get('MiniProgramName') is not None:
            self.mini_program_name = m.get('MiniProgramName')

        if m.get('MiniResourceId') is not None:
            self.mini_resource_id = m.get('MiniResourceId')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('QrCodeUrl') is not None:
            self.qr_code_url = m.get('QrCodeUrl')

        if m.get('ReviewTargetType') is not None:
            self.review_target_type = m.get('ReviewTargetType')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetGameReviewByStatusResponseBodyResultContentContentReviewProgress(DaraModel):
    def __init__(
        self,
        description: str = None,
        flow_node_id: int = None,
        gmt_modified: str = None,
        node_index: int = None,
        node_name: str = None,
        node_status: str = None,
        node_status_id: int = None,
        operator: str = None,
        remark: str = None,
        role_id: int = None,
    ):
        self.description = description
        self.flow_node_id = flow_node_id
        self.gmt_modified = gmt_modified
        self.node_index = node_index
        self.node_name = node_name
        self.node_status = node_status
        self.node_status_id = node_status_id
        self.operator = operator
        self.remark = remark
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.flow_node_id is not None:
            result['FlowNodeId'] = self.flow_node_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.node_index is not None:
            result['NodeIndex'] = self.node_index

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.node_status_id is not None:
            result['NodeStatusId'] = self.node_status_id

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowNodeId') is not None:
            self.flow_node_id = m.get('FlowNodeId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('NodeIndex') is not None:
            self.node_index = m.get('NodeIndex')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('NodeStatusId') is not None:
            self.node_status_id = m.get('NodeStatusId')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

