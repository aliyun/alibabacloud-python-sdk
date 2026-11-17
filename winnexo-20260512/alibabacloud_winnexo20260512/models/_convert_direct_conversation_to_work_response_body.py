# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertDirectConversationToWorkResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        conversion_id: str = None,
        converted_rounds: int = None,
        history_scope: str = None,
        message: str = None,
        request_id: str = None,
        retryable: bool = None,
        source_epoch: int = None,
        source_session_id: str = None,
        status: str = None,
        target_session_id: str = None,
        through_sequence: int = None,
        work_mode: str = None,
    ):
        # 业务状态码：成功为 200，失败沿现有 OpenAPI/POP 错误合同返回；转换是否整体完成须同时检查 status
        self.code = code
        # 转换 ID，查询及恢复过程中保持不变
        self.conversion_id = conversion_id
        # 固定快照中转换的完整 direct 问答轮数，不受发送接口 directMaxHistoryRounds 限制
        self.converted_rounds = converted_rounds
        # 转换历史范围，固定为 direct；不包含普通 work 历史
        self.history_scope = history_scope
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 是否允许继续原转换；false 表示不另起执行，仍允许用同一源 sessionId 查询。重试或继续始终复用同一转换、目标及快照
        self.retryable = retryable
        # 冻结快照对应的源 direct 历史 epoch
        self.source_epoch = source_epoch
        # 源会话 ID，与请求 sessionId 一致
        self.source_session_id = source_session_id
        # 转换状态：processing 表示处理中；succeeded 表示模型导入、目标登记、展示投影及两侧就绪均完成。失败按 OpenAPI/POP 错误合同处理，不能仅凭 HTTP 200 判断转换成功
        self.status = status
        # 新的 work 目标会话 ID，与源 ID 不同；processing 时可能返回预分配 ID，仅 succeeded 后可使用；重复查询或恢复复用原目标
        self.target_session_id = target_session_id
        # 冻结快照包含的最后一个 direct 轮次序号；源会话后续轮次不自动加入目标
        self.through_sequence = through_sequence
        # 目标会话的工作模式，固定为 work
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.conversion_id is not None:
            result['conversionId'] = self.conversion_id

        if self.converted_rounds is not None:
            result['convertedRounds'] = self.converted_rounds

        if self.history_scope is not None:
            result['historyScope'] = self.history_scope

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.source_epoch is not None:
            result['sourceEpoch'] = self.source_epoch

        if self.source_session_id is not None:
            result['sourceSessionId'] = self.source_session_id

        if self.status is not None:
            result['status'] = self.status

        if self.target_session_id is not None:
            result['targetSessionId'] = self.target_session_id

        if self.through_sequence is not None:
            result['throughSequence'] = self.through_sequence

        if self.work_mode is not None:
            result['workMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('conversionId') is not None:
            self.conversion_id = m.get('conversionId')

        if m.get('convertedRounds') is not None:
            self.converted_rounds = m.get('convertedRounds')

        if m.get('historyScope') is not None:
            self.history_scope = m.get('historyScope')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('sourceEpoch') is not None:
            self.source_epoch = m.get('sourceEpoch')

        if m.get('sourceSessionId') is not None:
            self.source_session_id = m.get('sourceSessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('targetSessionId') is not None:
            self.target_session_id = m.get('targetSessionId')

        if m.get('throughSequence') is not None:
            self.through_sequence = m.get('throughSequence')

        if m.get('workMode') is not None:
            self.work_mode = m.get('workMode')

        return self

