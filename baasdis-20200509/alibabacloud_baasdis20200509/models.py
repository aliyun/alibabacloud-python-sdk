# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateEenterpriseDIDRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_unique_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.owner_unique_id = owner_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_unique_id is not None:
            result['OwnerUniqueID'] = self.owner_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerUniqueID') is not None:
            self.owner_unique_id = m.get('OwnerUniqueID')
        return self


class CreateEenterpriseDIDResponseBody(TeaModel):
    def __init__(
        self,
        did: str = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.did = did
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEenterpriseDIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEenterpriseDIDResponseBody = None,
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
            temp_model = CreateEenterpriseDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePersonalDIDRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_unique_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.owner_unique_id = owner_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_unique_id is not None:
            result['OwnerUniqueID'] = self.owner_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerUniqueID') is not None:
            self.owner_unique_id = m.get('OwnerUniqueID')
        return self


class CreatePersonalDIDResponseBody(TeaModel):
    def __init__(
        self,
        did: str = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.did = did
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePersonalDIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePersonalDIDResponseBody = None,
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
            temp_model = CreatePersonalDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantDIDRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateTenantDIDResponseBody(TeaModel):
    def __init__(
        self,
        did: str = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.did = did
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTenantDIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTenantDIDResponseBody = None,
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
            temp_model = CreateTenantDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDIDRequest(TeaModel):
    def __init__(
        self,
        did: str = None,
    ):
        # This parameter is required.
        self.did = did

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.did is not None:
            result['DID'] = self.did
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DID') is not None:
            self.did = m.get('DID')
        return self


class GetDIDResponseBody(TeaModel):
    def __init__(
        self,
        doc: str = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.doc = doc
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc is not None:
            result['Doc'] = self.doc
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Doc') is not None:
            self.doc = m.get('Doc')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDIDResponseBody = None,
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
            temp_model = GetDIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IssueNormalVerifiableVCRequestBareClaimStructBody(TeaModel):
    def __init__(
        self,
        claim: str = None,
        claim_type: str = None,
    ):
        # This parameter is required.
        self.claim = claim
        self.claim_type = claim_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim is not None:
            result['Claim'] = self.claim
        if self.claim_type is not None:
            result['ClaimType'] = self.claim_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Claim') is not None:
            self.claim = m.get('Claim')
        if m.get('ClaimType') is not None:
            self.claim_type = m.get('ClaimType')
        return self


class IssueNormalVerifiableVCRequest(TeaModel):
    def __init__(
        self,
        bare_claim_struct_body: List[IssueNormalVerifiableVCRequestBareClaimStructBody] = None,
        client_token: str = None,
        expiration: int = None,
        issuer: str = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.bare_claim_struct_body = bare_claim_struct_body
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.expiration = expiration
        # This parameter is required.
        self.issuer = issuer
        # This parameter is required.
        self.subject = subject

    def validate(self):
        if self.bare_claim_struct_body:
            for k in self.bare_claim_struct_body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BareClaimStructBody'] = []
        if self.bare_claim_struct_body is not None:
            for k in self.bare_claim_struct_body:
                result['BareClaimStructBody'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bare_claim_struct_body = []
        if m.get('BareClaimStructBody') is not None:
            for k in m.get('BareClaimStructBody'):
                temp_model = IssueNormalVerifiableVCRequestBareClaimStructBody()
                self.bare_claim_struct_body.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class IssueNormalVerifiableVCResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
        verifiable_claim_content: str = None,
        verifiable_claim_id: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success
        self.verifiable_claim_content = verifiable_claim_content
        self.verifiable_claim_id = verifiable_claim_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        if self.verifiable_claim_content is not None:
            result['VerifiableClaimContent'] = self.verifiable_claim_content
        if self.verifiable_claim_id is not None:
            result['VerifiableClaimId'] = self.verifiable_claim_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('VerifiableClaimContent') is not None:
            self.verifiable_claim_content = m.get('VerifiableClaimContent')
        if m.get('VerifiableClaimId') is not None:
            self.verifiable_claim_id = m.get('VerifiableClaimId')
        return self


class IssueNormalVerifiableVCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IssueNormalVerifiableVCResponseBody = None,
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
            temp_model = IssueNormalVerifiableVCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVCRequest(TeaModel):
    def __init__(
        self,
        issuer_did: str = None,
        vcid: str = None,
        vcstatus: str = None,
    ):
        # This parameter is required.
        self.issuer_did = issuer_did
        # This parameter is required.
        self.vcid = vcid
        # This parameter is required.
        self.vcstatus = vcstatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issuer_did is not None:
            result['IssuerDid'] = self.issuer_did
        if self.vcid is not None:
            result['VCId'] = self.vcid
        if self.vcstatus is not None:
            result['VCStatus'] = self.vcstatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssuerDid') is not None:
            self.issuer_did = m.get('IssuerDid')
        if m.get('VCId') is not None:
            self.vcid = m.get('VCId')
        if m.get('VCStatus') is not None:
            self.vcstatus = m.get('VCStatus')
        return self


class UpdateVCResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateVCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVCResponseBody = None,
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
            temp_model = UpdateVCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyVerifiableClaimRequest(TeaModel):
    def __init__(
        self,
        vccontent: str = None,
    ):
        # This parameter is required.
        self.vccontent = vccontent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vccontent is not None:
            result['VCContent'] = self.vccontent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VCContent') is not None:
            self.vccontent = m.get('VCContent')
        return self


class VerifyVerifiableClaimResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyVerifiableClaimResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyVerifiableClaimResponseBody = None,
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
            temp_model = VerifyVerifiableClaimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


