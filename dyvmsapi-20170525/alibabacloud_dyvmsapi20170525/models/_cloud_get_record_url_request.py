# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudGetRecordUrlRequest(DaraModel):
    def __init__(
        self,
        call_type: int = None,
        download: int = None,
        enterprise_id: int = None,
        record_file: str = None,
        record_format: int = None,
        record_side: int = None,
        record_type: str = None,
    ):
        # 呼叫类型；说明：开启分线录音时，获取客户侧或座席侧录音需要，recordFormat=1时有效，recordFormat=0时忽略。取值范围：1,2,4,5（数字含义：呼入,webcall,预览外呼,预测外呼）
        self.call_type = call_type
        # 是否下载；１为下载，空或０表示试听
        self.download = download
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 录音文件名；如7000101-20160815140025-01087120766-01087120766--record-sip-1-1471240825.87
        # 
        # This parameter is required.
        self.record_file = record_file
        # 录音文件类型；取值说明：0为mp3，1为wav，默认为mp3类型
        self.record_format = record_format
        # 分线录音录音侧；说明：开启分线录音时，获取客户侧或座席侧录音需要，recordFormat=1时有效，recordFormat=0时忽略。取值范围：1,2 (数字含义：客户侧，座席侧)recordSide不为空时，callType必选
        self.record_side = record_side
        # 录音类型，不填可根据 recordFile 解析；record:录音voicemail:留言tsi:彩铃、当开启号码录音状态识别，发起预览外呼，客户号码是手机且客户未接听时返回该地址 rasr:语音机器人客户侧录音 transfer:转接consult:咨询threeway:三方
        self.record_type = record_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.download is not None:
            result['Download'] = self.download

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.record_file is not None:
            result['RecordFile'] = self.record_file

        if self.record_format is not None:
            result['RecordFormat'] = self.record_format

        if self.record_side is not None:
            result['RecordSide'] = self.record_side

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('Download') is not None:
            self.download = m.get('Download')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('RecordFile') is not None:
            self.record_file = m.get('RecordFile')

        if m.get('RecordFormat') is not None:
            self.record_format = m.get('RecordFormat')

        if m.get('RecordSide') is not None:
            self.record_side = m.get('RecordSide')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        return self

