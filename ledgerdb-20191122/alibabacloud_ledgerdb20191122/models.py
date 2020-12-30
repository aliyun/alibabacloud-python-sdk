# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AcceptMemberRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        key_type: str = None,
        public_key: str = None,
    ):
        self.ledger_id = ledger_id
        self.key_type = key_type
        self.public_key = public_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        return self


class AcceptMemberResponseBody(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        request_id: str = None,
    ):
        self.member_id = member_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AcceptMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AcceptMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AcceptMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        client_token: str = None,
    ):
        self.ledger_id = ledger_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_endpoint_id: str = None,
    ):
        self.request_id = request_id
        self.vpc_endpoint_id = vpc_endpoint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_endpoint_id is not None:
            result['VpcEndpointId'] = self.vpc_endpoint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcEndpointId') is not None:
            self.vpc_endpoint_id = m.get('VpcEndpointId')
        return self


class CreateVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVpcEndpointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLedgerRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
    ):
        self.ledger_id = ledger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        return self


class DeleteLedgerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLedgerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLedgerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLedgerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMemberRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        member_id: str = None,
    ):
        self.ledger_id = ledger_id
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class DeleteMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        vpc_endpoint_id: str = None,
    ):
        self.ledger_id = ledger_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.vpc_endpoint_id = vpc_endpoint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_endpoint_id is not None:
            result['VpcEndpointId'] = self.vpc_endpoint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcEndpointId') is not None:
            self.vpc_endpoint_id = m.get('VpcEndpointId')
        return self


class DeleteVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVpcEndpointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLedgerRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
    ):
        self.ledger_id = ledger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        return self


class DescribeLedgerResponseBodyLedgerLastTimeAnchor(TeaModel):
    def __init__(
        self,
        journal_id: str = None,
        ledger_version: str = None,
        time_stamp: str = None,
        ledger_digest: str = None,
        ledger_digest_type: str = None,
        proof: str = None,
    ):
        self.journal_id = journal_id
        self.ledger_version = ledger_version
        self.time_stamp = time_stamp
        self.ledger_digest = ledger_digest
        self.ledger_digest_type = ledger_digest_type
        self.proof = proof

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.journal_id is not None:
            result['JournalId'] = self.journal_id
        if self.ledger_version is not None:
            result['LedgerVersion'] = self.ledger_version
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.ledger_digest is not None:
            result['LedgerDigest'] = self.ledger_digest
        if self.ledger_digest_type is not None:
            result['LedgerDigestType'] = self.ledger_digest_type
        if self.proof is not None:
            result['Proof'] = self.proof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JournalId') is not None:
            self.journal_id = m.get('JournalId')
        if m.get('LedgerVersion') is not None:
            self.ledger_version = m.get('LedgerVersion')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('LedgerDigest') is not None:
            self.ledger_digest = m.get('LedgerDigest')
        if m.get('LedgerDigestType') is not None:
            self.ledger_digest_type = m.get('LedgerDigestType')
        if m.get('Proof') is not None:
            self.proof = m.get('Proof')
        return self


class DescribeLedgerResponseBodyLedger(TeaModel):
    def __init__(
        self,
        storage_class: str = None,
        update_time: str = None,
        journal_count: int = None,
        ledger_description: str = None,
        create_time: str = None,
        ledger_type: str = None,
        last_time_anchor: DescribeLedgerResponseBodyLedgerLastTimeAnchor = None,
        ledger_id: str = None,
        region_id: str = None,
        member_count: int = None,
        ledger_status: str = None,
        time_anchor_count: int = None,
        zone_id: str = None,
        ledger_name: str = None,
        owner_ali_uid: str = None,
    ):
        self.storage_class = storage_class
        self.update_time = update_time
        self.journal_count = journal_count
        self.ledger_description = ledger_description
        self.create_time = create_time
        self.ledger_type = ledger_type
        self.last_time_anchor = last_time_anchor
        self.ledger_id = ledger_id
        self.region_id = region_id
        self.member_count = member_count
        self.ledger_status = ledger_status
        self.time_anchor_count = time_anchor_count
        self.zone_id = zone_id
        self.ledger_name = ledger_name
        self.owner_ali_uid = owner_ali_uid

    def validate(self):
        if self.last_time_anchor:
            self.last_time_anchor.validate()

    def to_map(self):
        result = dict()
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.journal_count is not None:
            result['JournalCount'] = self.journal_count
        if self.ledger_description is not None:
            result['LedgerDescription'] = self.ledger_description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ledger_type is not None:
            result['LedgerType'] = self.ledger_type
        if self.last_time_anchor is not None:
            result['LastTimeAnchor'] = self.last_time_anchor.to_map()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.ledger_status is not None:
            result['LedgerStatus'] = self.ledger_status
        if self.time_anchor_count is not None:
            result['TimeAnchorCount'] = self.time_anchor_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.ledger_name is not None:
            result['LedgerName'] = self.ledger_name
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('JournalCount') is not None:
            self.journal_count = m.get('JournalCount')
        if m.get('LedgerDescription') is not None:
            self.ledger_description = m.get('LedgerDescription')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LedgerType') is not None:
            self.ledger_type = m.get('LedgerType')
        if m.get('LastTimeAnchor') is not None:
            temp_model = DescribeLedgerResponseBodyLedgerLastTimeAnchor()
            self.last_time_anchor = temp_model.from_map(m['LastTimeAnchor'])
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('LedgerStatus') is not None:
            self.ledger_status = m.get('LedgerStatus')
        if m.get('TimeAnchorCount') is not None:
            self.time_anchor_count = m.get('TimeAnchorCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('LedgerName') is not None:
            self.ledger_name = m.get('LedgerName')
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')
        return self


class DescribeLedgerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ledger: DescribeLedgerResponseBodyLedger = None,
    ):
        self.request_id = request_id
        self.ledger = ledger

    def validate(self):
        if self.ledger:
            self.ledger.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ledger is not None:
            result['Ledger'] = self.ledger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ledger') is not None:
            temp_model = DescribeLedgerResponseBodyLedger()
            self.ledger = temp_model.from_map(m['Ledger'])
        return self


class DescribeLedgerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLedgerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLedgerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLedgersRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class DescribeLedgersResponseBodyLedgersLastTimeAnchor(TeaModel):
    def __init__(
        self,
        journal_id: str = None,
        ledger_version: str = None,
        time_stamp: str = None,
        ledger_digest: str = None,
        ledger_digest_type: str = None,
        proof: str = None,
    ):
        self.journal_id = journal_id
        self.ledger_version = ledger_version
        self.time_stamp = time_stamp
        self.ledger_digest = ledger_digest
        self.ledger_digest_type = ledger_digest_type
        self.proof = proof

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.journal_id is not None:
            result['JournalId'] = self.journal_id
        if self.ledger_version is not None:
            result['LedgerVersion'] = self.ledger_version
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.ledger_digest is not None:
            result['LedgerDigest'] = self.ledger_digest
        if self.ledger_digest_type is not None:
            result['LedgerDigestType'] = self.ledger_digest_type
        if self.proof is not None:
            result['Proof'] = self.proof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JournalId') is not None:
            self.journal_id = m.get('JournalId')
        if m.get('LedgerVersion') is not None:
            self.ledger_version = m.get('LedgerVersion')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('LedgerDigest') is not None:
            self.ledger_digest = m.get('LedgerDigest')
        if m.get('LedgerDigestType') is not None:
            self.ledger_digest_type = m.get('LedgerDigestType')
        if m.get('Proof') is not None:
            self.proof = m.get('Proof')
        return self


class DescribeLedgersResponseBodyLedgers(TeaModel):
    def __init__(
        self,
        storage_class: str = None,
        update_time: str = None,
        journal_count: int = None,
        ledger_description: str = None,
        create_time: str = None,
        ledger_type: str = None,
        last_time_anchor: DescribeLedgersResponseBodyLedgersLastTimeAnchor = None,
        ledger_id: str = None,
        region_id: str = None,
        member_count: int = None,
        ledger_status: str = None,
        time_anchor_count: int = None,
        zone_id: str = None,
        ledger_name: str = None,
        owner_ali_uid: str = None,
    ):
        self.storage_class = storage_class
        self.update_time = update_time
        self.journal_count = journal_count
        self.ledger_description = ledger_description
        self.create_time = create_time
        self.ledger_type = ledger_type
        self.last_time_anchor = last_time_anchor
        self.ledger_id = ledger_id
        self.region_id = region_id
        self.member_count = member_count
        self.ledger_status = ledger_status
        self.time_anchor_count = time_anchor_count
        self.zone_id = zone_id
        self.ledger_name = ledger_name
        self.owner_ali_uid = owner_ali_uid

    def validate(self):
        if self.last_time_anchor:
            self.last_time_anchor.validate()

    def to_map(self):
        result = dict()
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.journal_count is not None:
            result['JournalCount'] = self.journal_count
        if self.ledger_description is not None:
            result['LedgerDescription'] = self.ledger_description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ledger_type is not None:
            result['LedgerType'] = self.ledger_type
        if self.last_time_anchor is not None:
            result['LastTimeAnchor'] = self.last_time_anchor.to_map()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.ledger_status is not None:
            result['LedgerStatus'] = self.ledger_status
        if self.time_anchor_count is not None:
            result['TimeAnchorCount'] = self.time_anchor_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.ledger_name is not None:
            result['LedgerName'] = self.ledger_name
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('JournalCount') is not None:
            self.journal_count = m.get('JournalCount')
        if m.get('LedgerDescription') is not None:
            self.ledger_description = m.get('LedgerDescription')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LedgerType') is not None:
            self.ledger_type = m.get('LedgerType')
        if m.get('LastTimeAnchor') is not None:
            temp_model = DescribeLedgersResponseBodyLedgersLastTimeAnchor()
            self.last_time_anchor = temp_model.from_map(m['LastTimeAnchor'])
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('LedgerStatus') is not None:
            self.ledger_status = m.get('LedgerStatus')
        if m.get('TimeAnchorCount') is not None:
            self.time_anchor_count = m.get('TimeAnchorCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('LedgerName') is not None:
            self.ledger_name = m.get('LedgerName')
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')
        return self


class DescribeLedgersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        ledgers: List[DescribeLedgersResponseBodyLedgers] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.ledgers = ledgers

    def validate(self):
        if self.ledgers:
            for k in self.ledgers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Ledgers'] = []
        if self.ledgers is not None:
            for k in self.ledgers:
                result['Ledgers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.ledgers = []
        if m.get('Ledgers') is not None:
            for k in m.get('Ledgers'):
                temp_model = DescribeLedgersResponseBodyLedgers()
                self.ledgers.append(temp_model.from_map(k))
        return self


class DescribeLedgersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLedgersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLedgersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        error_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.regions = regions
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTSARequest(TeaModel):
    def __init__(
        self,
        sequence_within_ledger: int = None,
    ):
        self.sequence_within_ledger = sequence_within_ledger

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sequence_within_ledger is not None:
            result['SequenceWithinLedger'] = self.sequence_within_ledger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SequenceWithinLedger') is not None:
            self.sequence_within_ledger = m.get('SequenceWithinLedger')
        return self


class DescribeTSAResponseBodyTSADetail(TeaModel):
    def __init__(
        self,
        ts: int = None,
        sn: str = None,
        root_hash: str = None,
        block_number: int = None,
        ctsr: str = None,
    ):
        self.ts = ts
        self.sn = sn
        self.root_hash = root_hash
        self.block_number = block_number
        self.ctsr = ctsr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ts is not None:
            result['TS'] = self.ts
        if self.sn is not None:
            result['SN'] = self.sn
        if self.root_hash is not None:
            result['RootHash'] = self.root_hash
        if self.block_number is not None:
            result['BlockNumber'] = self.block_number
        if self.ctsr is not None:
            result['CTSR'] = self.ctsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TS') is not None:
            self.ts = m.get('TS')
        if m.get('SN') is not None:
            self.sn = m.get('SN')
        if m.get('RootHash') is not None:
            self.root_hash = m.get('RootHash')
        if m.get('BlockNumber') is not None:
            self.block_number = m.get('BlockNumber')
        if m.get('CTSR') is not None:
            self.ctsr = m.get('CTSR')
        return self


class DescribeTSAResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tsadetail: DescribeTSAResponseBodyTSADetail = None,
    ):
        self.request_id = request_id
        self.tsadetail = tsadetail

    def validate(self):
        if self.tsadetail:
            self.tsadetail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tsadetail is not None:
            result['TSADetail'] = self.tsadetail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TSADetail') is not None:
            temp_model = DescribeTSAResponseBodyTSADetail()
            self.tsadetail = temp_model.from_map(m['TSADetail'])
        return self


class DescribeTSAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTSAResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTSAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableMemberRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        member_id: str = None,
    ):
        self.ledger_id = ledger_id
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class DisableMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableMemberRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        member_id: str = None,
    ):
        self.ledger_id = ledger_id
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class EnableMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessAttributeRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
    ):
        self.ledger_id = ledger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        return self


class GetAccessAttributeResponseBody(TeaModel):
    def __init__(
        self,
        enable_open_access: str = None,
        request_id: str = None,
        ledger_id: str = None,
        open_uri: str = None,
    ):
        self.enable_open_access = enable_open_access
        self.request_id = request_id
        self.ledger_id = ledger_id
        self.open_uri = open_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable_open_access is not None:
            result['EnableOpenAccess'] = self.enable_open_access
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.open_uri is not None:
            result['OpenUri'] = self.open_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOpenAccess') is not None:
            self.enable_open_access = m.get('EnableOpenAccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('OpenUri') is not None:
            self.open_uri = m.get('OpenUri')
        return self


class GetAccessAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccessAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccessAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
    ):
        self.ledger_id = ledger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        return self


class GetIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_list: str = None,
        ledger_id: str = None,
    ):
        self.request_id = request_id
        self.ip_list = ip_list
        self.ledger_id = ledger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        return self


class GetIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIpWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJournalRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        journal_id: int = None,
    ):
        self.ledger_id = ledger_id
        self.journal_id = journal_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.journal_id is not None:
            result['JournalId'] = self.journal_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('JournalId') is not None:
            self.journal_id = m.get('JournalId')
        return self


class GetJournalResponseBodyJournal(TeaModel):
    def __init__(
        self,
        journal_id: str = None,
        clues: List[str] = None,
        payload_json_string: str = None,
        journal_hash: str = None,
        timestamp: int = None,
        ledger_id: str = None,
        member_id: str = None,
        payload_type: str = None,
        client_id: str = None,
    ):
        self.journal_id = journal_id
        self.clues = clues
        self.payload_json_string = payload_json_string
        self.journal_hash = journal_hash
        self.timestamp = timestamp
        self.ledger_id = ledger_id
        self.member_id = member_id
        self.payload_type = payload_type
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.journal_id is not None:
            result['JournalId'] = self.journal_id
        if self.clues is not None:
            result['Clues'] = self.clues
        if self.payload_json_string is not None:
            result['PayloadJsonString'] = self.payload_json_string
        if self.journal_hash is not None:
            result['JournalHash'] = self.journal_hash
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.payload_type is not None:
            result['PayloadType'] = self.payload_type
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JournalId') is not None:
            self.journal_id = m.get('JournalId')
        if m.get('Clues') is not None:
            self.clues = m.get('Clues')
        if m.get('PayloadJsonString') is not None:
            self.payload_json_string = m.get('PayloadJsonString')
        if m.get('JournalHash') is not None:
            self.journal_hash = m.get('JournalHash')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('PayloadType') is not None:
            self.payload_type = m.get('PayloadType')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class GetJournalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        journal: GetJournalResponseBodyJournal = None,
    ):
        self.request_id = request_id
        self.journal = journal

    def validate(self):
        if self.journal:
            self.journal.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.journal is not None:
            result['Journal'] = self.journal.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Journal') is not None:
            temp_model = GetJournalResponseBodyJournal()
            self.journal = temp_model.from_map(m['Journal'])
        return self


class GetJournalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJournalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetJournalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMemberRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        member_id: str = None,
    ):
        self.ledger_id = ledger_id
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class GetMemberResponseBody(TeaModel):
    def __init__(
        self,
        kmskey_id: str = None,
        key_type: str = None,
        request_id: str = None,
        public_key: str = None,
        create_time: int = None,
        ledger_id: str = None,
        key_source: str = None,
        role: str = None,
        member_id: str = None,
        state: str = None,
        update_time: int = None,
        kmskey_version: str = None,
        key_meta: str = None,
        ali_uid: str = None,
    ):
        self.kmskey_id = kmskey_id
        self.key_type = key_type
        self.request_id = request_id
        self.public_key = public_key
        self.create_time = create_time
        self.ledger_id = ledger_id
        self.key_source = key_source
        self.role = role
        self.member_id = member_id
        self.state = state
        self.update_time = update_time
        self.kmskey_version = kmskey_version
        self.key_meta = key_meta
        self.ali_uid = ali_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.key_source is not None:
            result['KeySource'] = self.key_source
        if self.role is not None:
            result['Role'] = self.role
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.kmskey_version is not None:
            result['KMSKeyVersion'] = self.kmskey_version
        if self.key_meta is not None:
            result['KeyMeta'] = self.key_meta
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('KeySource') is not None:
            self.key_source = m.get('KeySource')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('KMSKeyVersion') is not None:
            self.kmskey_version = m.get('KMSKeyVersion')
        if m.get('KeyMeta') is not None:
            self.key_meta = m.get('KeyMeta')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        return self


class GetMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
    ):
        self.ledger_id = ledger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        return self


class GrantServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        slrstatus: str = None,
        request_id: str = None,
    ):
        self.slrstatus = slrstatus
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.slrstatus is not None:
            result['SLRStatus'] = self.slrstatus
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLRStatus') is not None:
            self.slrstatus = m.get('SLRStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GrantServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GrantServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InviteMembersRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        ali_uids: str = None,
    ):
        self.ledger_id = ledger_id
        self.ali_uids = ali_uids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.ali_uids is not None:
            result['AliUids'] = self.ali_uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('AliUids') is not None:
            self.ali_uids = m.get('AliUids')
        return self


class InviteMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InviteMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InviteMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InviteMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJournalsRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        clue: str = None,
        member_id: str = None,
        next_token: str = None,
        max_results: int = None,
        reverse: bool = None,
    ):
        self.ledger_id = ledger_id
        self.clue = clue
        self.member_id = member_id
        self.next_token = next_token
        self.max_results = max_results
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.clue is not None:
            result['Clue'] = self.clue
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('Clue') is not None:
            self.clue = m.get('Clue')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class ListJournalsResponseBodyJournals(TeaModel):
    def __init__(
        self,
        journal_id: str = None,
        clues: List[str] = None,
        payload_json_string: str = None,
        journal_hash: str = None,
        timestamp: int = None,
        ledger_id: str = None,
        member_id: str = None,
        payload_type: str = None,
        client_id: str = None,
    ):
        self.journal_id = journal_id
        self.clues = clues
        self.payload_json_string = payload_json_string
        self.journal_hash = journal_hash
        self.timestamp = timestamp
        self.ledger_id = ledger_id
        self.member_id = member_id
        self.payload_type = payload_type
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.journal_id is not None:
            result['JournalId'] = self.journal_id
        if self.clues is not None:
            result['Clues'] = self.clues
        if self.payload_json_string is not None:
            result['PayloadJsonString'] = self.payload_json_string
        if self.journal_hash is not None:
            result['JournalHash'] = self.journal_hash
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.payload_type is not None:
            result['PayloadType'] = self.payload_type
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JournalId') is not None:
            self.journal_id = m.get('JournalId')
        if m.get('Clues') is not None:
            self.clues = m.get('Clues')
        if m.get('PayloadJsonString') is not None:
            self.payload_json_string = m.get('PayloadJsonString')
        if m.get('JournalHash') is not None:
            self.journal_hash = m.get('JournalHash')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('PayloadType') is not None:
            self.payload_type = m.get('PayloadType')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class ListJournalsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        journals: List[ListJournalsResponseBodyJournals] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.journals = journals

    def validate(self):
        if self.journals:
            for k in self.journals:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Journals'] = []
        if self.journals is not None:
            for k in self.journals:
                result['Journals'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.journals = []
        if m.get('Journals') is not None:
            for k in m.get('Journals'):
                temp_model = ListJournalsResponseBodyJournals()
                self.journals.append(temp_model.from_map(k))
        return self


class ListJournalsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJournalsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListJournalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMembersRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.ledger_id = ledger_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListMembersResponseBodyMembers(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        key_type: str = None,
        state: str = None,
        create_time: int = None,
        public_key: str = None,
        ali_uid: str = None,
        member_id: str = None,
        ledger_id: str = None,
        role: str = None,
    ):
        self.update_time = update_time
        self.key_type = key_type
        self.state = state
        self.create_time = create_time
        self.public_key = public_key
        self.ali_uid = ali_uid
        self.member_id = member_id
        self.ledger_id = ledger_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListMembersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        members: List[ListMembersResponseBodyMembers] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = ListMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        return self


class ListMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTimeAnchorsRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        reverse: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.ledger_id = ledger_id
        self.reverse = reverse
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListTimeAnchorsResponseBodyTimeAnchors(TeaModel):
    def __init__(
        self,
        journal_id: int = None,
        ledger_version: int = None,
        time_stamp: int = None,
        ledger_digest: str = None,
        ledger_digest_type: str = None,
        proof: str = None,
    ):
        self.journal_id = journal_id
        self.ledger_version = ledger_version
        self.time_stamp = time_stamp
        self.ledger_digest = ledger_digest
        self.ledger_digest_type = ledger_digest_type
        self.proof = proof

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.journal_id is not None:
            result['JournalId'] = self.journal_id
        if self.ledger_version is not None:
            result['LedgerVersion'] = self.ledger_version
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.ledger_digest is not None:
            result['LedgerDigest'] = self.ledger_digest
        if self.ledger_digest_type is not None:
            result['LedgerDigestType'] = self.ledger_digest_type
        if self.proof is not None:
            result['Proof'] = self.proof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JournalId') is not None:
            self.journal_id = m.get('JournalId')
        if m.get('LedgerVersion') is not None:
            self.ledger_version = m.get('LedgerVersion')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('LedgerDigest') is not None:
            self.ledger_digest = m.get('LedgerDigest')
        if m.get('LedgerDigestType') is not None:
            self.ledger_digest_type = m.get('LedgerDigestType')
        if m.get('Proof') is not None:
            self.proof = m.get('Proof')
        return self


class ListTimeAnchorsResponseBody(TeaModel):
    def __init__(
        self,
        time_anchors: List[ListTimeAnchorsResponseBodyTimeAnchors] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.time_anchors = time_anchors
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.time_anchors:
            for k in self.time_anchors:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TimeAnchors'] = []
        if self.time_anchors is not None:
            for k in self.time_anchors:
                result['TimeAnchors'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_anchors = []
        if m.get('TimeAnchors') is not None:
            for k in m.get('TimeAnchors'):
                temp_model = ListTimeAnchorsResponseBodyTimeAnchors()
                self.time_anchors.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListTimeAnchorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTimeAnchorsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTimeAnchorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointsRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.ledger_id = ledger_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListVpcEndpointsResponseBodyVpcEndpoints(TeaModel):
    def __init__(
        self,
        status: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        create_time: int = None,
        address: str = None,
        vpc_endpoint_id: str = None,
        member_id: str = None,
        ledger_id: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.create_time = create_time
        self.address = address
        self.vpc_endpoint_id = vpc_endpoint_id
        self.member_id = member_id
        self.ledger_id = ledger_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.address is not None:
            result['Address'] = self.address
        if self.vpc_endpoint_id is not None:
            result['VpcEndpointId'] = self.vpc_endpoint_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('VpcEndpointId') is not None:
            self.vpc_endpoint_id = m.get('VpcEndpointId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpcEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        vpc_endpoints: List[ListVpcEndpointsResponseBodyVpcEndpoints] = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.vpc_endpoints = vpc_endpoints
        self.max_results = max_results

    def validate(self):
        if self.vpc_endpoints:
            for k in self.vpc_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VpcEndpoints'] = []
        if self.vpc_endpoints is not None:
            for k in self.vpc_endpoints:
                result['VpcEndpoints'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vpc_endpoints = []
        if m.get('VpcEndpoints') is not None:
            for k in m.get('VpcEndpoints'):
                temp_model = ListVpcEndpointsResponseBodyVpcEndpoints()
                self.vpc_endpoints.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListVpcEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVpcEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessAttributeRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        enable_open_access: bool = None,
    ):
        self.ledger_id = ledger_id
        self.enable_open_access = enable_open_access

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.enable_open_access is not None:
            result['EnableOpenAccess'] = self.enable_open_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('EnableOpenAccess') is not None:
            self.enable_open_access = m.get('EnableOpenAccess')
        return self


class ModifyAccessAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccessAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccessAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAccessAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        modify_type: str = None,
        ip_list: str = None,
    ):
        self.ledger_id = ledger_id
        self.modify_type = modify_type
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class ModifyIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyIpWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLedgerAttributeRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        ledger_name: str = None,
        ledger_description: str = None,
    ):
        self.ledger_id = ledger_id
        self.ledger_name = ledger_name
        self.ledger_description = ledger_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.ledger_name is not None:
            result['LedgerName'] = self.ledger_name
        if self.ledger_description is not None:
            result['LedgerDescription'] = self.ledger_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('LedgerName') is not None:
            self.ledger_name = m.get('LedgerName')
        if m.get('LedgerDescription') is not None:
            self.ledger_description = m.get('LedgerDescription')
        return self


class ModifyLedgerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyLedgerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLedgerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLedgerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMemberACLsRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        member_id: str = None,
        role: str = None,
    ):
        self.ledger_id = ledger_id
        self.member_id = member_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ModifyMemberACLsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyMemberACLsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyMemberACLsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyMemberACLsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMemberKeyRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        member_id: str = None,
        key_type: str = None,
        public_key: str = None,
    ):
        self.ledger_id = ledger_id
        self.member_id = member_id
        self.key_type = key_type
        self.public_key = public_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        return self


class ModifyMemberKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyMemberKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyMemberKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyMemberKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMemberKeyByKMSRequest(TeaModel):
    def __init__(
        self,
        ledger_id: str = None,
        member_id: str = None,
        key_type: str = None,
        kmskey_id: str = None,
        kmskey_version: str = None,
    ):
        self.ledger_id = ledger_id
        self.member_id = member_id
        self.key_type = key_type
        self.kmskey_id = kmskey_id
        self.kmskey_version = kmskey_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ledger_id is not None:
            result['LedgerId'] = self.ledger_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.kmskey_version is not None:
            result['KMSKeyVersion'] = self.kmskey_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedgerId') is not None:
            self.ledger_id = m.get('LedgerId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('KMSKeyVersion') is not None:
            self.kmskey_version = m.get('KMSKeyVersion')
        return self


class UpdateMemberKeyByKMSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMemberKeyByKMSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMemberKeyByKMSResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMemberKeyByKMSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


