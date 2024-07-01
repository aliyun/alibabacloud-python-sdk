# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AcknowledgeTaskResultRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        task_detail_no: List[str] = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.task_detail_no = task_detail_no
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class AcknowledgeTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: int = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AcknowledgeTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcknowledgeTaskResultResponseBody = None,
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
            temp_model = AcknowledgeTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchFuzzyMatchDomainSensitiveWordRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.keyword = keyword
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord(TeaModel):
    def __init__(
        self,
        word: str = None,
    ):
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords(TeaModel):
    def __init__(
        self,
        matched_sensitive_word: List[BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord] = None,
    ):
        self.matched_sensitive_word = matched_sensitive_word

    def validate(self):
        if self.matched_sensitive_word:
            for k in self.matched_sensitive_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchedSensitiveWord'] = []
        if self.matched_sensitive_word is not None:
            for k in self.matched_sensitive_word:
                result['MatchedSensitiveWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matched_sensitive_word = []
        if m.get('MatchedSensitiveWord') is not None:
            for k in m.get('MatchedSensitiveWord'):
                temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord()
                self.matched_sensitive_word.append(temp_model.from_map(k))
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult(TeaModel):
    def __init__(
        self,
        exist: bool = None,
        keyword: str = None,
        matched_sentive_words: BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords = None,
    ):
        self.exist = exist
        self.keyword = keyword
        self.matched_sentive_words = matched_sentive_words

    def validate(self):
        if self.matched_sentive_words:
            self.matched_sentive_words.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist is not None:
            result['Exist'] = self.exist
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.matched_sentive_words is not None:
            result['MatchedSentiveWords'] = self.matched_sentive_words.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MatchedSentiveWords') is not None:
            temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords()
            self.matched_sentive_words = temp_model.from_map(m['MatchedSentiveWords'])
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList(TeaModel):
    def __init__(
        self,
        sensitive_word_match_result: List[BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult] = None,
    ):
        self.sensitive_word_match_result = sensitive_word_match_result

    def validate(self):
        if self.sensitive_word_match_result:
            for k in self.sensitive_word_match_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SensitiveWordMatchResult'] = []
        if self.sensitive_word_match_result is not None:
            for k in self.sensitive_word_match_result:
                result['SensitiveWordMatchResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_word_match_result = []
        if m.get('SensitiveWordMatchResult') is not None:
            for k in m.get('SensitiveWordMatchResult'):
                temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult()
                self.sensitive_word_match_result.append(temp_model.from_map(k))
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sensitive_word_match_result_list: BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList = None,
    ):
        self.request_id = request_id
        self.sensitive_word_match_result_list = sensitive_word_match_result_list

    def validate(self):
        if self.sensitive_word_match_result_list:
            self.sensitive_word_match_result_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sensitive_word_match_result_list is not None:
            result['SensitiveWordMatchResultList'] = self.sensitive_word_match_result_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SensitiveWordMatchResultList') is not None:
            temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList()
            self.sensitive_word_match_result_list = temp_model.from_map(m['SensitiveWordMatchResultList'])
        return self


class BatchFuzzyMatchDomainSensitiveWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchFuzzyMatchDomainSensitiveWordResponseBody = None,
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
            temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDomainVerificationRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        instance_id: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.action_type = action_type
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CancelDomainVerificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelDomainVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelDomainVerificationResponseBody = None,
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
            temp_model = CancelDomainVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTaskRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        task_no: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.task_no = task_no
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CancelTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelTaskResponseBody = None,
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
            temp_model = CancelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        fee_command: str = None,
        fee_currency: str = None,
        fee_period: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.fee_command = fee_command
        self.fee_currency = fee_currency
        self.fee_period = fee_period
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.fee_command is not None:
            result['FeeCommand'] = self.fee_command
        if self.fee_currency is not None:
            result['FeeCurrency'] = self.fee_currency
        if self.fee_period is not None:
            result['FeePeriod'] = self.fee_period
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FeeCommand') is not None:
            self.fee_command = m.get('FeeCommand')
        if m.get('FeeCurrency') is not None:
            self.fee_currency = m.get('FeeCurrency')
        if m.get('FeePeriod') is not None:
            self.fee_period = m.get('FeePeriod')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CheckDomainResponseBody(TeaModel):
    def __init__(
        self,
        avail: str = None,
        domain_name: str = None,
        dynamic_check: bool = None,
        premium: str = None,
        price: int = None,
        reason: str = None,
        request_id: str = None,
    ):
        self.avail = avail
        self.domain_name = domain_name
        self.dynamic_check = dynamic_check
        self.premium = premium
        self.price = price
        self.reason = reason
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avail is not None:
            result['Avail'] = self.avail
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.dynamic_check is not None:
            result['DynamicCheck'] = self.dynamic_check
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.price is not None:
            result['Price'] = self.price
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avail') is not None:
            self.avail = m.get('Avail')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DynamicCheck') is not None:
            self.dynamic_check = m.get('DynamicCheck')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDomainResponseBody = None,
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
            temp_model = CheckDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainSunriseClaimRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CheckDomainSunriseClaimResponseBody(TeaModel):
    def __init__(
        self,
        claim_key: str = None,
        request_id: str = None,
        result: int = None,
    ):
        self.claim_key = claim_key
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_key is not None:
            result['ClaimKey'] = self.claim_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimKey') is not None:
            self.claim_key = m.get('ClaimKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckDomainSunriseClaimResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDomainSunriseClaimResponseBody = None,
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
            temp_model = CheckDomainSunriseClaimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTransferInFeasibilityRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        transfer_authorization_code: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.transfer_authorization_code = transfer_authorization_code
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.transfer_authorization_code is not None:
            result['TransferAuthorizationCode'] = self.transfer_authorization_code
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TransferAuthorizationCode') is not None:
            self.transfer_authorization_code = m.get('TransferAuthorizationCode')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CheckTransferInFeasibilityResponseBody(TeaModel):
    def __init__(
        self,
        can_transfer: bool = None,
        code: str = None,
        message: str = None,
        product_id: str = None,
        request_id: str = None,
    ):
        self.can_transfer = can_transfer
        self.code = code
        self.message = message
        self.product_id = product_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_transfer is not None:
            result['CanTransfer'] = self.can_transfer
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanTransfer') is not None:
            self.can_transfer = m.get('CanTransfer')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckTransferInFeasibilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckTransferInFeasibilityResponseBody = None,
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
            temp_model = CheckTransferInFeasibilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmTransferInEmailRequest(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        email: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.email = email
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class ConfirmTransferInEmailResponseBodyFailList(TeaModel):
    def __init__(
        self,
        fail_domain: List[str] = None,
    ):
        self.fail_domain = fail_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_domain is not None:
            result['FailDomain'] = self.fail_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailDomain') is not None:
            self.fail_domain = m.get('FailDomain')
        return self


class ConfirmTransferInEmailResponseBodySuccessList(TeaModel):
    def __init__(
        self,
        success_domain: List[str] = None,
    ):
        self.success_domain = success_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_domain is not None:
            result['SuccessDomain'] = self.success_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccessDomain') is not None:
            self.success_domain = m.get('SuccessDomain')
        return self


class ConfirmTransferInEmailResponseBody(TeaModel):
    def __init__(
        self,
        fail_list: ConfirmTransferInEmailResponseBodyFailList = None,
        request_id: str = None,
        success_list: ConfirmTransferInEmailResponseBodySuccessList = None,
    ):
        self.fail_list = fail_list
        self.request_id = request_id
        self.success_list = success_list

    def validate(self):
        if self.fail_list:
            self.fail_list.validate()
        if self.success_list:
            self.success_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_list is not None:
            result['FailList'] = self.fail_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_list is not None:
            result['SuccessList'] = self.success_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailList') is not None:
            temp_model = ConfirmTransferInEmailResponseBodyFailList()
            self.fail_list = temp_model.from_map(m['FailList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessList') is not None:
            temp_model = ConfirmTransferInEmailResponseBodySuccessList()
            self.success_list = temp_model.from_map(m['SuccessList'])
        return self


class ConfirmTransferInEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmTransferInEmailResponseBody = None,
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
            temp_model = ConfirmTransferInEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEmailVerificationRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.email = email
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DeleteEmailVerificationResponseBodyFailList(TeaModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteEmailVerificationResponseBodySuccessList(TeaModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteEmailVerificationResponseBody(TeaModel):
    def __init__(
        self,
        fail_list: List[DeleteEmailVerificationResponseBodyFailList] = None,
        request_id: str = None,
        success_list: List[DeleteEmailVerificationResponseBodySuccessList] = None,
    ):
        self.fail_list = fail_list
        self.request_id = request_id
        self.success_list = success_list

    def validate(self):
        if self.fail_list:
            for k in self.fail_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailList'] = []
        if self.fail_list is not None:
            for k in self.fail_list:
                result['FailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_list = []
        if m.get('FailList') is not None:
            for k in m.get('FailList'):
                temp_model = DeleteEmailVerificationResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = DeleteEmailVerificationResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class DeleteEmailVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEmailVerificationResponseBody = None,
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
            temp_model = DeleteEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistrantProfileRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DeleteRegistrantProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRegistrantProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRegistrantProfileResponseBody = None,
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
            temp_model = DeleteRegistrantProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmailVerifiedRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.email = email
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class EmailVerifiedResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EmailVerifiedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EmailVerifiedResponseBody = None,
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
            temp_model = EmailVerifiedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FuzzyMatchDomainSensitiveWordRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.keyword = keyword
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord(TeaModel):
    def __init__(
        self,
        word: str = None,
    ):
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords(TeaModel):
    def __init__(
        self,
        matched_sensitive_word: List[FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord] = None,
    ):
        self.matched_sensitive_word = matched_sensitive_word

    def validate(self):
        if self.matched_sensitive_word:
            for k in self.matched_sensitive_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchedSensitiveWord'] = []
        if self.matched_sensitive_word is not None:
            for k in self.matched_sensitive_word:
                result['MatchedSensitiveWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matched_sensitive_word = []
        if m.get('MatchedSensitiveWord') is not None:
            for k in m.get('MatchedSensitiveWord'):
                temp_model = FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord()
                self.matched_sensitive_word.append(temp_model.from_map(k))
        return self


class FuzzyMatchDomainSensitiveWordResponseBody(TeaModel):
    def __init__(
        self,
        exist: bool = None,
        keyword: str = None,
        matched_sentive_words: FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords = None,
        request_id: str = None,
    ):
        self.exist = exist
        self.keyword = keyword
        self.matched_sentive_words = matched_sentive_words
        self.request_id = request_id

    def validate(self):
        if self.matched_sentive_words:
            self.matched_sentive_words.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist is not None:
            result['Exist'] = self.exist
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.matched_sentive_words is not None:
            result['MatchedSentiveWords'] = self.matched_sentive_words.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MatchedSentiveWords') is not None:
            temp_model = FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords()
            self.matched_sentive_words = temp_model.from_map(m['MatchedSentiveWords'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FuzzyMatchDomainSensitiveWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FuzzyMatchDomainSensitiveWordResponseBody = None,
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
            temp_model = FuzzyMatchDomainSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmailVerificationRequest(TeaModel):
    def __init__(
        self,
        begin_create_time: int = None,
        email: str = None,
        end_create_time: int = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        user_client_ip: str = None,
        verification_status: int = None,
    ):
        self.begin_create_time = begin_create_time
        self.email = email
        self.end_create_time = end_create_time
        self.lang = lang
        self.page_num = page_num
        self.page_size = page_size
        self.user_client_ip = user_client_ip
        self.verification_status = verification_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time
        if self.email is not None:
            result['Email'] = self.email
        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListEmailVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        confirm_ip: str = None,
        email: str = None,
        email_verification_no: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        send_ip: str = None,
        token_send_time: str = None,
        user_id: str = None,
        verification_status: int = None,
        verification_time: str = None,
    ):
        self.confirm_ip = confirm_ip
        self.email = email
        self.email_verification_no = email_verification_no
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.send_ip = send_ip
        self.token_send_time = token_send_time
        self.user_id = user_id
        self.verification_status = verification_status
        self.verification_time = verification_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm_ip is not None:
            result['ConfirmIp'] = self.confirm_ip
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_no is not None:
            result['EmailVerificationNo'] = self.email_verification_no
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.send_ip is not None:
            result['SendIp'] = self.send_ip
        if self.token_send_time is not None:
            result['TokenSendTime'] = self.token_send_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.verification_time is not None:
            result['VerificationTime'] = self.verification_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmIp') is not None:
            self.confirm_ip = m.get('ConfirmIp')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationNo') is not None:
            self.email_verification_no = m.get('EmailVerificationNo')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('SendIp') is not None:
            self.send_ip = m.get('SendIp')
        if m.get('TokenSendTime') is not None:
            self.token_send_time = m.get('TokenSendTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('VerificationTime') is not None:
            self.verification_time = m.get('VerificationTime')
        return self


class ListEmailVerificationResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListEmailVerificationResponseBodyData] = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEmailVerificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListEmailVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEmailVerificationResponseBody = None,
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
            temp_model = ListEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LookupTmchNoticeRequest(TeaModel):
    def __init__(
        self,
        claim_key: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.claim_key = claim_key
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_key is not None:
            result['ClaimKey'] = self.claim_key
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimKey') is not None:
            self.claim_key = m.get('ClaimKey')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc(TeaModel):
    def __init__(
        self,
        class_num: int = None,
        desc: str = None,
    ):
        self.class_num = class_num
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_num is not None:
            result['ClassNum'] = self.class_num
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassNum') is not None:
            self.class_num = m.get('ClassNum')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimClassDescs(TeaModel):
    def __init__(
        self,
        class_desc: List[LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc] = None,
    ):
        self.class_desc = class_desc

    def validate(self):
        if self.class_desc:
            for k in self.class_desc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClassDesc'] = []
        if self.class_desc is not None:
            for k in self.class_desc:
                result['ClassDesc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_desc = []
        if m.get('ClassDesc') is not None:
            for k in m.get('ClassDesc'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc()
                self.class_desc.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet(TeaModel):
    def __init__(
        self,
        street: List[str] = None,
    ):
        self.street = street

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.street is not None:
            result['Street'] = self.street
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Street') is not None:
            self.street = m.get('Street')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr(TeaModel):
    def __init__(
        self,
        cc: str = None,
        city: str = None,
        pc: str = None,
        sp: str = None,
        street: LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet = None,
    ):
        self.cc = cc
        self.city = city
        self.pc = pc
        self.sp = sp
        self.street = street

    def validate(self):
        if self.street:
            self.street.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc
        if self.city is not None:
            result['City'] = self.city
        if self.pc is not None:
            result['Pc'] = self.pc
        if self.sp is not None:
            result['Sp'] = self.sp
        if self.street is not None:
            result['Street'] = self.street.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Pc') is not None:
            self.pc = m.get('Pc')
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        if m.get('Street') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet()
            self.street = temp_model.from_map(m['Street'])
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContactsContact(TeaModel):
    def __init__(
        self,
        addr: LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr = None,
        email: str = None,
        fax: str = None,
        name: str = None,
        org: str = None,
        type: str = None,
        voice: str = None,
    ):
        self.addr = addr
        self.email = email
        self.fax = fax
        self.name = name
        self.org = org
        self.type = type
        self.voice = voice

    def validate(self):
        if self.addr:
            self.addr.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()
        if self.email is not None:
            result['Email'] = self.email
        if self.fax is not None:
            result['Fax'] = self.fax
        if self.name is not None:
            result['Name'] = self.name
        if self.org is not None:
            result['Org'] = self.org
        if self.type is not None:
            result['Type'] = self.type
        if self.voice is not None:
            result['Voice'] = self.voice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr()
            self.addr = temp_model.from_map(m['Addr'])
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Fax') is not None:
            self.fax = m.get('Fax')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Org') is not None:
            self.org = m.get('Org')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContacts(TeaModel):
    def __init__(
        self,
        contact: List[LookupTmchNoticeResponseBodyClaimsClaimContactsContact] = None,
    ):
        self.contact = contact

    def validate(self):
        if self.contact:
            for k in self.contact:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contact'] = []
        if self.contact is not None:
            for k in self.contact:
                result['Contact'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact = []
        if m.get('Contact') is not None:
            for k in m.get('Contact'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaimContactsContact()
                self.contact.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet(TeaModel):
    def __init__(
        self,
        street: List[str] = None,
    ):
        self.street = street

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.street is not None:
            result['Street'] = self.street
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Street') is not None:
            self.street = m.get('Street')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr(TeaModel):
    def __init__(
        self,
        cc: str = None,
        city: str = None,
        pc: str = None,
        sp: str = None,
        street: LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet = None,
    ):
        self.cc = cc
        self.city = city
        self.pc = pc
        self.sp = sp
        self.street = street

    def validate(self):
        if self.street:
            self.street.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc
        if self.city is not None:
            result['City'] = self.city
        if self.pc is not None:
            result['Pc'] = self.pc
        if self.sp is not None:
            result['Sp'] = self.sp
        if self.street is not None:
            result['Street'] = self.street.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Pc') is not None:
            self.pc = m.get('Pc')
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        if m.get('Street') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet()
            self.street = temp_model.from_map(m['Street'])
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder(TeaModel):
    def __init__(
        self,
        addr: LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr = None,
        entitlement: str = None,
        org: str = None,
    ):
        self.addr = addr
        self.entitlement = entitlement
        self.org = org

    def validate(self):
        if self.addr:
            self.addr.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()
        if self.entitlement is not None:
            result['Entitlement'] = self.entitlement
        if self.org is not None:
            result['Org'] = self.org
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr()
            self.addr = temp_model.from_map(m['Addr'])
        if m.get('Entitlement') is not None:
            self.entitlement = m.get('Entitlement')
        if m.get('Org') is not None:
            self.org = m.get('Org')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHolders(TeaModel):
    def __init__(
        self,
        holder: List[LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder] = None,
    ):
        self.holder = holder

    def validate(self):
        if self.holder:
            for k in self.holder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Holder'] = []
        if self.holder is not None:
            for k in self.holder:
                result['Holder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.holder = []
        if m.get('Holder') is not None:
            for k in m.get('Holder'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder()
                self.holder.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBodyClaimsClaimJurDesc(TeaModel):
    def __init__(
        self,
        desc: str = None,
        jur_cc: str = None,
    ):
        self.desc = desc
        self.jur_cc = jur_cc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.jur_cc is not None:
            result['JurCC'] = self.jur_cc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('JurCC') is not None:
            self.jur_cc = m.get('JurCC')
        return self


class LookupTmchNoticeResponseBodyClaimsClaim(TeaModel):
    def __init__(
        self,
        class_descs: LookupTmchNoticeResponseBodyClaimsClaimClassDescs = None,
        contacts: LookupTmchNoticeResponseBodyClaimsClaimContacts = None,
        goods_and_services: str = None,
        holders: LookupTmchNoticeResponseBodyClaimsClaimHolders = None,
        jur_desc: LookupTmchNoticeResponseBodyClaimsClaimJurDesc = None,
        mark_name: str = None,
    ):
        self.class_descs = class_descs
        self.contacts = contacts
        self.goods_and_services = goods_and_services
        self.holders = holders
        self.jur_desc = jur_desc
        self.mark_name = mark_name

    def validate(self):
        if self.class_descs:
            self.class_descs.validate()
        if self.contacts:
            self.contacts.validate()
        if self.holders:
            self.holders.validate()
        if self.jur_desc:
            self.jur_desc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_descs is not None:
            result['ClassDescs'] = self.class_descs.to_map()
        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()
        if self.goods_and_services is not None:
            result['GoodsAndServices'] = self.goods_and_services
        if self.holders is not None:
            result['Holders'] = self.holders.to_map()
        if self.jur_desc is not None:
            result['JurDesc'] = self.jur_desc.to_map()
        if self.mark_name is not None:
            result['MarkName'] = self.mark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassDescs') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimClassDescs()
            self.class_descs = temp_model.from_map(m['ClassDescs'])
        if m.get('Contacts') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimContacts()
            self.contacts = temp_model.from_map(m['Contacts'])
        if m.get('GoodsAndServices') is not None:
            self.goods_and_services = m.get('GoodsAndServices')
        if m.get('Holders') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimHolders()
            self.holders = temp_model.from_map(m['Holders'])
        if m.get('JurDesc') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimJurDesc()
            self.jur_desc = temp_model.from_map(m['JurDesc'])
        if m.get('MarkName') is not None:
            self.mark_name = m.get('MarkName')
        return self


class LookupTmchNoticeResponseBodyClaims(TeaModel):
    def __init__(
        self,
        claim: List[LookupTmchNoticeResponseBodyClaimsClaim] = None,
    ):
        self.claim = claim

    def validate(self):
        if self.claim:
            for k in self.claim:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Claim'] = []
        if self.claim is not None:
            for k in self.claim:
                result['Claim'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.claim = []
        if m.get('Claim') is not None:
            for k in m.get('Claim'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaim()
                self.claim.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBody(TeaModel):
    def __init__(
        self,
        claims: LookupTmchNoticeResponseBodyClaims = None,
        id: int = None,
        label: str = None,
        not_after: str = None,
        not_before: str = None,
        request_id: str = None,
    ):
        self.claims = claims
        self.id = id
        self.label = label
        self.not_after = not_after
        self.not_before = not_before
        self.request_id = request_id

    def validate(self):
        if self.claims:
            self.claims.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claims is not None:
            result['Claims'] = self.claims.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Claims') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaims()
            self.claims = temp_model.from_map(m['Claims'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LookupTmchNoticeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LookupTmchNoticeResponseBody = None,
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
            temp_model = LookupTmchNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PollTaskResultRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        instance_id: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        task_no: str = None,
        task_result_status: int = None,
        user_client_ip: str = None,
    ):
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.lang = lang
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.task_no = task_no
        self.task_result_status = task_result_status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_result_status is not None:
            result['TaskResultStatus'] = self.task_result_status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskResultStatus') is not None:
            self.task_result_status = m.get('TaskResultStatus')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class PollTaskResultResponseBodyDataTaskDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_result: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_result = task_result
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class PollTaskResultResponseBodyData(TeaModel):
    def __init__(
        self,
        task_detail: List[PollTaskResultResponseBodyDataTaskDetail] = None,
    ):
        self.task_detail = task_detail

    def validate(self):
        if self.task_detail:
            for k in self.task_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskDetail'] = []
        if self.task_detail is not None:
            for k in self.task_detail:
                result['TaskDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_detail = []
        if m.get('TaskDetail') is not None:
            for k in m.get('TaskDetail'):
                temp_model = PollTaskResultResponseBodyDataTaskDetail()
                self.task_detail.append(temp_model.from_map(k))
        return self


class PollTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: PollTaskResultResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = PollTaskResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class PollTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PollTaskResultResponseBody = None,
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
            temp_model = PollTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryArtExtensionRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryArtExtensionResponseBody(TeaModel):
    def __init__(
        self,
        date_or_period: str = None,
        dimensions: str = None,
        features: str = None,
        inscriptions_and_markings: str = None,
        maker: str = None,
        materials_and_techniques: str = None,
        object_type: str = None,
        reference: str = None,
        request_id: str = None,
        subject: str = None,
        title: str = None,
    ):
        self.date_or_period = date_or_period
        self.dimensions = dimensions
        self.features = features
        self.inscriptions_and_markings = inscriptions_and_markings
        self.maker = maker
        self.materials_and_techniques = materials_and_techniques
        self.object_type = object_type
        self.reference = reference
        self.request_id = request_id
        self.subject = subject
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_or_period is not None:
            result['DateOrPeriod'] = self.date_or_period
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.features is not None:
            result['Features'] = self.features
        if self.inscriptions_and_markings is not None:
            result['InscriptionsAndMarkings'] = self.inscriptions_and_markings
        if self.maker is not None:
            result['Maker'] = self.maker
        if self.materials_and_techniques is not None:
            result['MaterialsAndTechniques'] = self.materials_and_techniques
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.reference is not None:
            result['Reference'] = self.reference
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateOrPeriod') is not None:
            self.date_or_period = m.get('DateOrPeriod')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InscriptionsAndMarkings') is not None:
            self.inscriptions_and_markings = m.get('InscriptionsAndMarkings')
        if m.get('Maker') is not None:
            self.maker = m.get('Maker')
        if m.get('MaterialsAndTechniques') is not None:
            self.materials_and_techniques = m.get('MaterialsAndTechniques')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class QueryArtExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryArtExtensionResponseBody = None,
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
            temp_model = QueryArtExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChangeLogListRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_date: int = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        start_date: int = None,
        user_client_ip: str = None,
    ):
        self.domain_name = domain_name
        self.end_date = end_date
        self.lang = lang
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.start_date = start_date
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryChangeLogListResponseBodyDataChangeLog(TeaModel):
    def __init__(
        self,
        details: str = None,
        domain_name: str = None,
        operation: str = None,
        operation_ipaddress: str = None,
        result: str = None,
        time: str = None,
    ):
        self.details = details
        self.domain_name = domain_name
        self.operation = operation
        self.operation_ipaddress = operation_ipaddress
        self.result = result
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.details is not None:
            result['Details'] = self.details
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.operation_ipaddress is not None:
            result['OperationIPAddress'] = self.operation_ipaddress
        if self.result is not None:
            result['Result'] = self.result
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OperationIPAddress') is not None:
            self.operation_ipaddress = m.get('OperationIPAddress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryChangeLogListResponseBodyData(TeaModel):
    def __init__(
        self,
        change_log: List[QueryChangeLogListResponseBodyDataChangeLog] = None,
    ):
        self.change_log = change_log

    def validate(self):
        if self.change_log:
            for k in self.change_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeLog'] = []
        if self.change_log is not None:
            for k in self.change_log:
                result['ChangeLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_log = []
        if m.get('ChangeLog') is not None:
            for k in m.get('ChangeLog'):
                temp_model = QueryChangeLogListResponseBodyDataChangeLog()
                self.change_log.append(temp_model.from_map(k))
        return self


class QueryChangeLogListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryChangeLogListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.result_limit = result_limit
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryChangeLogListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryChangeLogListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChangeLogListResponseBody = None,
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
            temp_model = QueryChangeLogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryContactInfoRequest(TeaModel):
    def __init__(
        self,
        contact_type: str = None,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.contact_type = contact_type
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryContactInfoResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        create_date: str = None,
        email: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        request_id: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        self.create_date = create_date
        self.email = email
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.request_id = request_id
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.email is not None:
            result['Email'] = self.email
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class QueryContactInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryContactInfoResponseBody = None,
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
            temp_model = QueryContactInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDSRecordRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDSRecordResponseBodyDSRecordList(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        digest: str = None,
        digest_type: int = None,
        key_tag: int = None,
    ):
        self.algorithm = algorithm
        self.digest = digest
        self.digest_type = digest_type
        self.key_tag = key_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_type is not None:
            result['DigestType'] = self.digest_type
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        return self


class QueryDSRecordResponseBody(TeaModel):
    def __init__(
        self,
        dsrecord_list: List[QueryDSRecordResponseBodyDSRecordList] = None,
        request_id: str = None,
    ):
        self.dsrecord_list = dsrecord_list
        self.request_id = request_id

    def validate(self):
        if self.dsrecord_list:
            for k in self.dsrecord_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DSRecordList'] = []
        if self.dsrecord_list is not None:
            for k in self.dsrecord_list:
                result['DSRecordList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dsrecord_list = []
        if m.get('DSRecordList') is not None:
            for k in m.get('DSRecordList'):
                temp_model = QueryDSRecordResponseBodyDSRecordList()
                self.dsrecord_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDSRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDSRecordResponseBody = None,
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
            temp_model = QueryDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDnsHostRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDnsHostResponseBodyDnsHostList(TeaModel):
    def __init__(
        self,
        dns_name: str = None,
        ip_list: List[str] = None,
    ):
        self.dns_name = dns_name
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class QueryDnsHostResponseBody(TeaModel):
    def __init__(
        self,
        dns_host_list: List[QueryDnsHostResponseBodyDnsHostList] = None,
        request_id: str = None,
    ):
        self.dns_host_list = dns_host_list
        self.request_id = request_id

    def validate(self):
        if self.dns_host_list:
            for k in self.dns_host_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DnsHostList'] = []
        if self.dns_host_list is not None:
            for k in self.dns_host_list:
                result['DnsHostList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_host_list = []
        if m.get('DnsHostList') is not None:
            for k in m.get('DnsHostList'):
                temp_model = QueryDnsHostResponseBodyDnsHostList()
                self.dns_host_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDnsHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDnsHostResponseBody = None,
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
            temp_model = QueryDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainByDomainNameRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainByDomainNameResponseBodyDnsList(TeaModel):
    def __init__(
        self,
        dns: List[str] = None,
    ):
        self.dns = dns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns is not None:
            result['Dns'] = self.dns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')
        return self


class QueryDomainByDomainNameResponseBody(TeaModel):
    def __init__(
        self,
        dns_list: QueryDomainByDomainNameResponseBodyDnsList = None,
        domain_name: str = None,
        domain_name_proxy_service: bool = None,
        domain_name_verification_status: str = None,
        email: str = None,
        email_verification_client_hold: bool = None,
        email_verification_status: int = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        instance_id: str = None,
        premium: bool = None,
        real_name_status: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        registrant_updating_status: str = None,
        registration_date: str = None,
        registration_date_long: int = None,
        request_id: str = None,
        transfer_out_status: str = None,
        transfer_prohibition_lock: str = None,
        update_prohibition_lock: str = None,
        user_id: str = None,
    ):
        self.dns_list = dns_list
        self.domain_name = domain_name
        self.domain_name_proxy_service = domain_name_proxy_service
        self.domain_name_verification_status = domain_name_verification_status
        self.email = email
        self.email_verification_client_hold = email_verification_client_hold
        self.email_verification_status = email_verification_status
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.instance_id = instance_id
        self.premium = premium
        self.real_name_status = real_name_status
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_type = registrant_type
        self.registrant_updating_status = registrant_updating_status
        self.registration_date = registration_date
        self.registration_date_long = registration_date_long
        self.request_id = request_id
        self.transfer_out_status = transfer_out_status
        self.transfer_prohibition_lock = transfer_prohibition_lock
        self.update_prohibition_lock = update_prohibition_lock
        self.user_id = user_id

    def validate(self):
        if self.dns_list:
            self.dns_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_list is not None:
            result['DnsList'] = self.dns_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_proxy_service is not None:
            result['DomainNameProxyService'] = self.domain_name_proxy_service
        if self.domain_name_verification_status is not None:
            result['DomainNameVerificationStatus'] = self.domain_name_verification_status
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_client_hold is not None:
            result['EmailVerificationClientHold'] = self.email_verification_client_hold
        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.registrant_updating_status is not None:
            result['RegistrantUpdatingStatus'] = self.registrant_updating_status
        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date
        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_out_status is not None:
            result['TransferOutStatus'] = self.transfer_out_status
        if self.transfer_prohibition_lock is not None:
            result['TransferProhibitionLock'] = self.transfer_prohibition_lock
        if self.update_prohibition_lock is not None:
            result['UpdateProhibitionLock'] = self.update_prohibition_lock
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsList') is not None:
            temp_model = QueryDomainByDomainNameResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m['DnsList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameProxyService') is not None:
            self.domain_name_proxy_service = m.get('DomainNameProxyService')
        if m.get('DomainNameVerificationStatus') is not None:
            self.domain_name_verification_status = m.get('DomainNameVerificationStatus')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationClientHold') is not None:
            self.email_verification_client_hold = m.get('EmailVerificationClientHold')
        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('RegistrantUpdatingStatus') is not None:
            self.registrant_updating_status = m.get('RegistrantUpdatingStatus')
        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')
        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferOutStatus') is not None:
            self.transfer_out_status = m.get('TransferOutStatus')
        if m.get('TransferProhibitionLock') is not None:
            self.transfer_prohibition_lock = m.get('TransferProhibitionLock')
        if m.get('UpdateProhibitionLock') is not None:
            self.update_prohibition_lock = m.get('UpdateProhibitionLock')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryDomainByDomainNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDomainByDomainNameResponseBody = None,
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
            temp_model = QueryDomainByDomainNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainByInstanceIdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainByInstanceIdResponseBodyDnsList(TeaModel):
    def __init__(
        self,
        dns: List[str] = None,
    ):
        self.dns = dns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns is not None:
            result['Dns'] = self.dns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')
        return self


class QueryDomainByInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        dns_list: QueryDomainByInstanceIdResponseBodyDnsList = None,
        domain_name: str = None,
        domain_name_proxy_service: bool = None,
        domain_name_verification_status: str = None,
        email: str = None,
        email_verification_client_hold: bool = None,
        email_verification_status: int = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        instance_id: str = None,
        premium: bool = None,
        real_name_status: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        registrant_updating_status: str = None,
        registration_date: str = None,
        registration_date_long: int = None,
        request_id: str = None,
        transfer_out_status: str = None,
        transfer_prohibition_lock: str = None,
        update_prohibition_lock: str = None,
        user_id: str = None,
    ):
        self.dns_list = dns_list
        self.domain_name = domain_name
        self.domain_name_proxy_service = domain_name_proxy_service
        self.domain_name_verification_status = domain_name_verification_status
        self.email = email
        self.email_verification_client_hold = email_verification_client_hold
        self.email_verification_status = email_verification_status
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.instance_id = instance_id
        self.premium = premium
        self.real_name_status = real_name_status
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_type = registrant_type
        self.registrant_updating_status = registrant_updating_status
        self.registration_date = registration_date
        self.registration_date_long = registration_date_long
        self.request_id = request_id
        self.transfer_out_status = transfer_out_status
        self.transfer_prohibition_lock = transfer_prohibition_lock
        self.update_prohibition_lock = update_prohibition_lock
        self.user_id = user_id

    def validate(self):
        if self.dns_list:
            self.dns_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_list is not None:
            result['DnsList'] = self.dns_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_proxy_service is not None:
            result['DomainNameProxyService'] = self.domain_name_proxy_service
        if self.domain_name_verification_status is not None:
            result['DomainNameVerificationStatus'] = self.domain_name_verification_status
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_client_hold is not None:
            result['EmailVerificationClientHold'] = self.email_verification_client_hold
        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.registrant_updating_status is not None:
            result['RegistrantUpdatingStatus'] = self.registrant_updating_status
        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date
        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_out_status is not None:
            result['TransferOutStatus'] = self.transfer_out_status
        if self.transfer_prohibition_lock is not None:
            result['TransferProhibitionLock'] = self.transfer_prohibition_lock
        if self.update_prohibition_lock is not None:
            result['UpdateProhibitionLock'] = self.update_prohibition_lock
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsList') is not None:
            temp_model = QueryDomainByInstanceIdResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m['DnsList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameProxyService') is not None:
            self.domain_name_proxy_service = m.get('DomainNameProxyService')
        if m.get('DomainNameVerificationStatus') is not None:
            self.domain_name_verification_status = m.get('DomainNameVerificationStatus')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationClientHold') is not None:
            self.email_verification_client_hold = m.get('EmailVerificationClientHold')
        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('RegistrantUpdatingStatus') is not None:
            self.registrant_updating_status = m.get('RegistrantUpdatingStatus')
        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')
        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferOutStatus') is not None:
            self.transfer_out_status = m.get('TransferOutStatus')
        if m.get('TransferProhibitionLock') is not None:
            self.transfer_prohibition_lock = m.get('TransferProhibitionLock')
        if m.get('UpdateProhibitionLock') is not None:
            self.update_prohibition_lock = m.get('UpdateProhibitionLock')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryDomainByInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDomainByInstanceIdResponseBody = None,
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
            temp_model = QueryDomainByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainListRequest(TeaModel):
    def __init__(
        self,
        ccompany: str = None,
        domain_name: str = None,
        end_expiration_date: int = None,
        end_registration_date: int = None,
        lang: str = None,
        order_by_type: str = None,
        order_key_type: str = None,
        page_num: int = None,
        page_size: int = None,
        product_domain_type: str = None,
        query_type: str = None,
        start_expiration_date: int = None,
        start_registration_date: int = None,
        user_client_ip: str = None,
    ):
        self.ccompany = ccompany
        self.domain_name = domain_name
        self.end_expiration_date = end_expiration_date
        self.end_registration_date = end_registration_date
        self.lang = lang
        self.order_by_type = order_by_type
        self.order_key_type = order_key_type
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.product_domain_type = product_domain_type
        self.query_type = query_type
        self.start_expiration_date = start_expiration_date
        self.start_registration_date = start_registration_date
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ccompany is not None:
            result['Ccompany'] = self.ccompany
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_expiration_date is not None:
            result['EndExpirationDate'] = self.end_expiration_date
        if self.end_registration_date is not None:
            result['EndRegistrationDate'] = self.end_registration_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order_by_type is not None:
            result['OrderByType'] = self.order_by_type
        if self.order_key_type is not None:
            result['OrderKeyType'] = self.order_key_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_domain_type is not None:
            result['ProductDomainType'] = self.product_domain_type
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.start_expiration_date is not None:
            result['StartExpirationDate'] = self.start_expiration_date
        if self.start_registration_date is not None:
            result['StartRegistrationDate'] = self.start_registration_date
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ccompany') is not None:
            self.ccompany = m.get('Ccompany')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndExpirationDate') is not None:
            self.end_expiration_date = m.get('EndExpirationDate')
        if m.get('EndRegistrationDate') is not None:
            self.end_registration_date = m.get('EndRegistrationDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OrderByType') is not None:
            self.order_by_type = m.get('OrderByType')
        if m.get('OrderKeyType') is not None:
            self.order_key_type = m.get('OrderKeyType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductDomainType') is not None:
            self.product_domain_type = m.get('ProductDomainType')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('StartExpirationDate') is not None:
            self.start_expiration_date = m.get('StartExpirationDate')
        if m.get('StartRegistrationDate') is not None:
            self.start_registration_date = m.get('StartRegistrationDate')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainListResponseBodyDataDomain(TeaModel):
    def __init__(
        self,
        domain_audit_status: str = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_type: str = None,
        expiration_curr_date_diff: int = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        expiration_date_status: str = None,
        instance_id: str = None,
        premium: bool = None,
        product_id: str = None,
        registrant_type: str = None,
        registration_date: str = None,
        registration_date_long: int = None,
        remark: str = None,
    ):
        self.domain_audit_status = domain_audit_status
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.domain_type = domain_type
        self.expiration_curr_date_diff = expiration_curr_date_diff
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.expiration_date_status = expiration_date_status
        self.instance_id = instance_id
        self.premium = premium
        self.product_id = product_id
        self.registrant_type = registrant_type
        self.registration_date = registration_date
        self.registration_date_long = registration_date_long
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_audit_status is not None:
            result['DomainAuditStatus'] = self.domain_audit_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.expiration_curr_date_diff is not None:
            result['ExpirationCurrDateDiff'] = self.expiration_curr_date_diff
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.expiration_date_status is not None:
            result['ExpirationDateStatus'] = self.expiration_date_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date
        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainAuditStatus') is not None:
            self.domain_audit_status = m.get('DomainAuditStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('ExpirationCurrDateDiff') is not None:
            self.expiration_curr_date_diff = m.get('ExpirationCurrDateDiff')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('ExpirationDateStatus') is not None:
            self.expiration_date_status = m.get('ExpirationDateStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')
        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class QueryDomainListResponseBodyData(TeaModel):
    def __init__(
        self,
        domain: List[QueryDomainListResponseBodyDataDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['Domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k in m.get('Domain'):
                temp_model = QueryDomainListResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class QueryDomainListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryDomainListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryDomainListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDomainListResponseBody = None,
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
            temp_model = QueryDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainRealNameVerificationInfoRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        fetch_image: bool = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.fetch_image = fetch_image
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.fetch_image is not None:
            result['FetchImage'] = self.fetch_image
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FetchImage') is not None:
            self.fetch_image = m.get('FetchImage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainRealNameVerificationInfoResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        identity_credential_url: str = None,
        instance_id: str = None,
        request_id: str = None,
        submission_date: str = None,
    ):
        self.domain_name = domain_name
        self.identity_credential = identity_credential
        self.identity_credential_no = identity_credential_no
        self.identity_credential_type = identity_credential_type
        self.identity_credential_url = identity_credential_url
        self.instance_id = instance_id
        self.request_id = request_id
        self.submission_date = submission_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.identity_credential_url is not None:
            result['IdentityCredentialUrl'] = self.identity_credential_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('IdentityCredentialUrl') is not None:
            self.identity_credential_url = m.get('IdentityCredentialUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        return self


class QueryDomainRealNameVerificationInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDomainRealNameVerificationInfoResponseBody = None,
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
            temp_model = QueryDomainRealNameVerificationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEnsAssociationRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryEnsAssociationResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        request_id: str = None,
    ):
        self.address = address
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryEnsAssociationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEnsAssociationResponseBody = None,
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
            temp_model = QueryEnsAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFailReasonForDomainRealNameVerificationRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        real_name_verification_action: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.real_name_verification_action = real_name_verification_action
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.real_name_verification_action is not None:
            result['RealNameVerificationAction'] = self.real_name_verification_action
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RealNameVerificationAction') is not None:
            self.real_name_verification_action = m.get('RealNameVerificationAction')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryFailReasonForDomainRealNameVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        fail_reason: str = None,
    ):
        self.date = date
        self.fail_reason = fail_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        return self


class QueryFailReasonForDomainRealNameVerificationResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryFailReasonForDomainRealNameVerificationResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryFailReasonForDomainRealNameVerificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryFailReasonForDomainRealNameVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFailReasonForDomainRealNameVerificationResponseBody = None,
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
            temp_model = QueryFailReasonForDomainRealNameVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileID'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileID') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileID')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        fail_reason: str = None,
    ):
        self.date = date
        self.fail_reason = fail_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryFailReasonForRegistrantProfileRealNameVerificationResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryFailReasonForRegistrantProfileRealNameVerificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFailReasonForRegistrantProfileRealNameVerificationResponseBody = None,
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
            temp_model = QueryFailReasonForRegistrantProfileRealNameVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLocalEnsAssociationRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryLocalEnsAssociationResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        request_id: str = None,
    ):
        self.address = address
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryLocalEnsAssociationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLocalEnsAssociationResponseBody = None,
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
            temp_model = QueryLocalEnsAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRegistrantProfileRealNameVerificationInfoRequest(TeaModel):
    def __init__(
        self,
        fetch_image: bool = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        self.fetch_image = fetch_image
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_image is not None:
            result['FetchImage'] = self.fetch_image
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchImage') is not None:
            self.fetch_image = m.get('FetchImage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryRegistrantProfileRealNameVerificationInfoResponseBody(TeaModel):
    def __init__(
        self,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        identity_credential_url: str = None,
        modification_date: str = None,
        registrant_profile_id: int = None,
        request_id: str = None,
        submission_date: str = None,
    ):
        self.identity_credential = identity_credential
        self.identity_credential_no = identity_credential_no
        self.identity_credential_type = identity_credential_type
        self.identity_credential_url = identity_credential_url
        self.modification_date = modification_date
        self.registrant_profile_id = registrant_profile_id
        self.request_id = request_id
        self.submission_date = submission_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.identity_credential_url is not None:
            result['IdentityCredentialUrl'] = self.identity_credential_url
        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('IdentityCredentialUrl') is not None:
            self.identity_credential_url = m.get('IdentityCredentialUrl')
        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        return self


class QueryRegistrantProfileRealNameVerificationInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRegistrantProfileRealNameVerificationInfoResponseBody = None,
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
            temp_model = QueryRegistrantProfileRealNameVerificationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRegistrantProfilesRequest(TeaModel):
    def __init__(
        self,
        default_registrant_profile: bool = None,
        email: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        real_name_status: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_profile_type: str = None,
        registrant_type: str = None,
        user_client_ip: str = None,
    ):
        self.default_registrant_profile = default_registrant_profile
        self.email = email
        self.lang = lang
        self.page_num = page_num
        self.page_size = page_size
        self.real_name_status = real_name_status
        self.registrant_organization = registrant_organization
        self.registrant_profile_id = registrant_profile_id
        self.registrant_profile_type = registrant_profile_type
        self.registrant_type = registrant_type
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        create_time: str = None,
        default_registrant_profile: bool = None,
        email: str = None,
        email_verification_status: int = None,
        postal_code: str = None,
        province: str = None,
        real_name_status: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_profile_type: str = None,
        registrant_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        update_time: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        self.create_time = create_time
        self.default_registrant_profile = default_registrant_profile
        self.email = email
        self.email_verification_status = email_verification_status
        self.postal_code = postal_code
        self.province = province
        self.real_name_status = real_name_status
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_profile_id = registrant_profile_id
        self.registrant_profile_type = registrant_profile_type
        self.registrant_type = registrant_type
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryRegistrantProfilesResponseBodyRegistrantProfiles(TeaModel):
    def __init__(
        self,
        registrant_profile: List[QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile] = None,
    ):
        self.registrant_profile = registrant_profile

    def validate(self):
        if self.registrant_profile:
            for k in self.registrant_profile:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegistrantProfile'] = []
        if self.registrant_profile is not None:
            for k in self.registrant_profile:
                result['RegistrantProfile'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.registrant_profile = []
        if m.get('RegistrantProfile') is not None:
            for k in m.get('RegistrantProfile'):
                temp_model = QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile()
                self.registrant_profile.append(temp_model.from_map(k))
        return self


class QueryRegistrantProfilesResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        registrant_profiles: QueryRegistrantProfilesResponseBodyRegistrantProfiles = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.registrant_profiles = registrant_profiles
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.registrant_profiles:
            self.registrant_profiles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.registrant_profiles is not None:
            result['RegistrantProfiles'] = self.registrant_profiles.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RegistrantProfiles') is not None:
            temp_model = QueryRegistrantProfilesResponseBodyRegistrantProfiles()
            self.registrant_profiles = temp_model.from_map(m['RegistrantProfiles'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryRegistrantProfilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRegistrantProfilesResponseBody = None,
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
            temp_model = QueryRegistrantProfilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskDetailHistoryRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_name_cursor: str = None,
        lang: str = None,
        page_size: int = None,
        task_detail_no_cursor: str = None,
        task_no: str = None,
        task_status: int = None,
        user_client_ip: str = None,
    ):
        self.domain_name = domain_name
        self.domain_name_cursor = domain_name_cursor
        self.lang = lang
        # This parameter is required.
        self.page_size = page_size
        self.task_detail_no_cursor = task_detail_no_cursor
        # This parameter is required.
        self.task_no = task_no
        self.task_status = task_status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_cursor is not None:
            result['DomainNameCursor'] = self.domain_name_cursor
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_detail_no_cursor is not None:
            result['TaskDetailNoCursor'] = self.task_detail_no_cursor
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameCursor') is not None:
            self.domain_name_cursor = m.get('DomainNameCursor')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskDetailNoCursor') is not None:
            self.task_detail_no_cursor = m.get('TaskDetailNoCursor')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskDetailHistoryResponseBodyCurrentPageCursor(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBodyNextPageCursor(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBodyObjects(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBodyPrePageCursor(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBody(TeaModel):
    def __init__(
        self,
        current_page_cursor: QueryTaskDetailHistoryResponseBodyCurrentPageCursor = None,
        next_page_cursor: QueryTaskDetailHistoryResponseBodyNextPageCursor = None,
        objects: List[QueryTaskDetailHistoryResponseBodyObjects] = None,
        page_size: int = None,
        pre_page_cursor: QueryTaskDetailHistoryResponseBodyPrePageCursor = None,
        request_id: str = None,
    ):
        self.current_page_cursor = current_page_cursor
        self.next_page_cursor = next_page_cursor
        self.objects = objects
        self.page_size = page_size
        self.pre_page_cursor = pre_page_cursor
        self.request_id = request_id

    def validate(self):
        if self.current_page_cursor:
            self.current_page_cursor.validate()
        if self.next_page_cursor:
            self.next_page_cursor.validate()
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()
        if self.pre_page_cursor:
            self.pre_page_cursor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_cursor is not None:
            result['CurrentPageCursor'] = self.current_page_cursor.to_map()
        if self.next_page_cursor is not None:
            result['NextPageCursor'] = self.next_page_cursor.to_map()
        result['Objects'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Objects'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page_cursor is not None:
            result['PrePageCursor'] = self.pre_page_cursor.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageCursor') is not None:
            temp_model = QueryTaskDetailHistoryResponseBodyCurrentPageCursor()
            self.current_page_cursor = temp_model.from_map(m['CurrentPageCursor'])
        if m.get('NextPageCursor') is not None:
            temp_model = QueryTaskDetailHistoryResponseBodyNextPageCursor()
            self.next_page_cursor = temp_model.from_map(m['NextPageCursor'])
        self.objects = []
        if m.get('Objects') is not None:
            for k in m.get('Objects'):
                temp_model = QueryTaskDetailHistoryResponseBodyObjects()
                self.objects.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePageCursor') is not None:
            temp_model = QueryTaskDetailHistoryResponseBodyPrePageCursor()
            self.pre_page_cursor = temp_model.from_map(m['PrePageCursor'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTaskDetailHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskDetailHistoryResponseBody = None,
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
            temp_model = QueryTaskDetailHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskDetailListRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        instance_id: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        task_no: str = None,
        task_status: int = None,
        user_client_ip: str = None,
    ):
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.lang = lang
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.task_no = task_no
        self.task_status = task_status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskDetailListResponseBodyDataTaskDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_result: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain_name = domain_name
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.task_detail_no = task_detail_no
        self.task_no = task_no
        self.task_result = task_result
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description
        self.try_count = try_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailListResponseBodyData(TeaModel):
    def __init__(
        self,
        task_detail: List[QueryTaskDetailListResponseBodyDataTaskDetail] = None,
    ):
        self.task_detail = task_detail

    def validate(self):
        if self.task_detail:
            for k in self.task_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskDetail'] = []
        if self.task_detail is not None:
            for k in self.task_detail:
                result['TaskDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_detail = []
        if m.get('TaskDetail') is not None:
            for k in m.get('TaskDetail'):
                temp_model = QueryTaskDetailListResponseBodyDataTaskDetail()
                self.task_detail.append(temp_model.from_map(k))
        return self


class QueryTaskDetailListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTaskDetailListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTaskDetailListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTaskDetailListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskDetailListResponseBody = None,
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
            temp_model = QueryTaskDetailListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskInfoHistoryRequest(TeaModel):
    def __init__(
        self,
        begin_create_time: int = None,
        create_time_cursor: int = None,
        end_create_time: int = None,
        lang: str = None,
        page_size: int = None,
        task_no_cursor: str = None,
        user_client_ip: str = None,
    ):
        self.begin_create_time = begin_create_time
        self.create_time_cursor = create_time_cursor
        self.end_create_time = end_create_time
        self.lang = lang
        # This parameter is required.
        self.page_size = page_size
        self.task_no_cursor = task_no_cursor
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time
        if self.create_time_cursor is not None:
            result['CreateTimeCursor'] = self.create_time_cursor
        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_no_cursor is not None:
            result['TaskNoCursor'] = self.task_no_cursor
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')
        if m.get('CreateTimeCursor') is not None:
            self.create_time_cursor = m.get('CreateTimeCursor')
        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskNoCursor') is not None:
            self.task_no_cursor = m.get('TaskNoCursor')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskInfoHistoryResponseBodyCurrentPageCursor(TeaModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        self.clientip = clientip
        self.create_time = create_time
        self.create_time_long = create_time_long
        self.task_no = task_no
        self.task_num = task_num
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBodyNextPageCursor(TeaModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        self.clientip = clientip
        self.create_time = create_time
        self.create_time_long = create_time_long
        self.task_no = task_no
        self.task_num = task_num
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBodyObjects(TeaModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        self.clientip = clientip
        self.create_time = create_time
        self.create_time_long = create_time_long
        self.task_no = task_no
        self.task_num = task_num
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBodyPrePageCursor(TeaModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        self.clientip = clientip
        self.create_time = create_time
        self.create_time_long = create_time_long
        self.task_no = task_no
        self.task_num = task_num
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBody(TeaModel):
    def __init__(
        self,
        current_page_cursor: QueryTaskInfoHistoryResponseBodyCurrentPageCursor = None,
        next_page_cursor: QueryTaskInfoHistoryResponseBodyNextPageCursor = None,
        objects: List[QueryTaskInfoHistoryResponseBodyObjects] = None,
        page_size: int = None,
        pre_page_cursor: QueryTaskInfoHistoryResponseBodyPrePageCursor = None,
        request_id: str = None,
    ):
        self.current_page_cursor = current_page_cursor
        self.next_page_cursor = next_page_cursor
        self.objects = objects
        self.page_size = page_size
        self.pre_page_cursor = pre_page_cursor
        self.request_id = request_id

    def validate(self):
        if self.current_page_cursor:
            self.current_page_cursor.validate()
        if self.next_page_cursor:
            self.next_page_cursor.validate()
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()
        if self.pre_page_cursor:
            self.pre_page_cursor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_cursor is not None:
            result['CurrentPageCursor'] = self.current_page_cursor.to_map()
        if self.next_page_cursor is not None:
            result['NextPageCursor'] = self.next_page_cursor.to_map()
        result['Objects'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Objects'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page_cursor is not None:
            result['PrePageCursor'] = self.pre_page_cursor.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageCursor') is not None:
            temp_model = QueryTaskInfoHistoryResponseBodyCurrentPageCursor()
            self.current_page_cursor = temp_model.from_map(m['CurrentPageCursor'])
        if m.get('NextPageCursor') is not None:
            temp_model = QueryTaskInfoHistoryResponseBodyNextPageCursor()
            self.next_page_cursor = temp_model.from_map(m['NextPageCursor'])
        self.objects = []
        if m.get('Objects') is not None:
            for k in m.get('Objects'):
                temp_model = QueryTaskInfoHistoryResponseBodyObjects()
                self.objects.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePageCursor') is not None:
            temp_model = QueryTaskInfoHistoryResponseBodyPrePageCursor()
            self.pre_page_cursor = temp_model.from_map(m['PrePageCursor'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTaskInfoHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskInfoHistoryResponseBody = None,
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
            temp_model = QueryTaskInfoHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskListRequest(TeaModel):
    def __init__(
        self,
        begin_create_time: int = None,
        end_create_time: int = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        user_client_ip: str = None,
    ):
        self.begin_create_time = begin_create_time
        self.end_create_time = end_create_time
        self.lang = lang
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time
        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')
        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskListResponseBodyDataTaskInfo(TeaModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        task_cancel_status: str = None,
        task_cancel_status_code: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        self.clientip = clientip
        self.create_time = create_time
        self.task_cancel_status = task_cancel_status
        self.task_cancel_status_code = task_cancel_status_code
        self.task_no = task_no
        self.task_num = task_num
        self.task_status = task_status
        self.task_status_code = task_status_code
        self.task_type = task_type
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_cancel_status is not None:
            result['TaskCancelStatus'] = self.task_cancel_status
        if self.task_cancel_status_code is not None:
            result['TaskCancelStatusCode'] = self.task_cancel_status_code
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskCancelStatus') is not None:
            self.task_cancel_status = m.get('TaskCancelStatus')
        if m.get('TaskCancelStatusCode') is not None:
            self.task_cancel_status_code = m.get('TaskCancelStatusCode')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskListResponseBodyData(TeaModel):
    def __init__(
        self,
        task_info: List[QueryTaskListResponseBodyDataTaskInfo] = None,
    ):
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            for k in self.task_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskInfo'] = []
        if self.task_info is not None:
            for k in self.task_info:
                result['TaskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_info = []
        if m.get('TaskInfo') is not None:
            for k in m.get('TaskInfo'):
                temp_model = QueryTaskListResponseBodyDataTaskInfo()
                self.task_info.append(temp_model.from_map(k))
        return self


class QueryTaskListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTaskListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTaskListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskListResponseBody = None,
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
            temp_model = QueryTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferInByInstanceIdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTransferInByInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        email: str = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        instance_id: str = None,
        modification_date: str = None,
        modification_date_long: int = None,
        need_mail_check: bool = None,
        progress_bar_type: int = None,
        request_id: str = None,
        result_code: str = None,
        result_date: str = None,
        result_date_long: int = None,
        result_msg: str = None,
        simple_transfer_in_status: str = None,
        status: int = None,
        submission_date: str = None,
        submission_date_long: int = None,
        transfer_authorization_code_submission_date: str = None,
        transfer_authorization_code_submission_date_long: int = None,
        user_id: str = None,
        whois_mail_status: bool = None,
    ):
        self.domain_name = domain_name
        self.email = email
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.instance_id = instance_id
        self.modification_date = modification_date
        self.modification_date_long = modification_date_long
        self.need_mail_check = need_mail_check
        self.progress_bar_type = progress_bar_type
        self.request_id = request_id
        self.result_code = result_code
        self.result_date = result_date
        self.result_date_long = result_date_long
        self.result_msg = result_msg
        self.simple_transfer_in_status = simple_transfer_in_status
        self.status = status
        self.submission_date = submission_date
        self.submission_date_long = submission_date_long
        self.transfer_authorization_code_submission_date = transfer_authorization_code_submission_date
        self.transfer_authorization_code_submission_date_long = transfer_authorization_code_submission_date_long
        self.user_id = user_id
        self.whois_mail_status = whois_mail_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date
        if self.modification_date_long is not None:
            result['ModificationDateLong'] = self.modification_date_long
        if self.need_mail_check is not None:
            result['NeedMailCheck'] = self.need_mail_check
        if self.progress_bar_type is not None:
            result['ProgressBarType'] = self.progress_bar_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_date is not None:
            result['ResultDate'] = self.result_date
        if self.result_date_long is not None:
            result['ResultDateLong'] = self.result_date_long
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        if self.submission_date_long is not None:
            result['SubmissionDateLong'] = self.submission_date_long
        if self.transfer_authorization_code_submission_date is not None:
            result['TransferAuthorizationCodeSubmissionDate'] = self.transfer_authorization_code_submission_date
        if self.transfer_authorization_code_submission_date_long is not None:
            result['TransferAuthorizationCodeSubmissionDateLong'] = self.transfer_authorization_code_submission_date_long
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.whois_mail_status is not None:
            result['WhoisMailStatus'] = self.whois_mail_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')
        if m.get('ModificationDateLong') is not None:
            self.modification_date_long = m.get('ModificationDateLong')
        if m.get('NeedMailCheck') is not None:
            self.need_mail_check = m.get('NeedMailCheck')
        if m.get('ProgressBarType') is not None:
            self.progress_bar_type = m.get('ProgressBarType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultDate') is not None:
            self.result_date = m.get('ResultDate')
        if m.get('ResultDateLong') is not None:
            self.result_date_long = m.get('ResultDateLong')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        if m.get('SubmissionDateLong') is not None:
            self.submission_date_long = m.get('SubmissionDateLong')
        if m.get('TransferAuthorizationCodeSubmissionDate') is not None:
            self.transfer_authorization_code_submission_date = m.get('TransferAuthorizationCodeSubmissionDate')
        if m.get('TransferAuthorizationCodeSubmissionDateLong') is not None:
            self.transfer_authorization_code_submission_date_long = m.get('TransferAuthorizationCodeSubmissionDateLong')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WhoisMailStatus') is not None:
            self.whois_mail_status = m.get('WhoisMailStatus')
        return self


class QueryTransferInByInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTransferInByInstanceIdResponseBody = None,
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
            temp_model = QueryTransferInByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferInListRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        simple_transfer_in_status: str = None,
        submission_end_date: int = None,
        submission_start_date: int = None,
        user_client_ip: str = None,
    ):
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.simple_transfer_in_status = simple_transfer_in_status
        self.submission_end_date = submission_end_date
        self.submission_start_date = submission_start_date
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status
        if self.submission_end_date is not None:
            result['SubmissionEndDate'] = self.submission_end_date
        if self.submission_start_date is not None:
            result['SubmissionStartDate'] = self.submission_start_date
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')
        if m.get('SubmissionEndDate') is not None:
            self.submission_end_date = m.get('SubmissionEndDate')
        if m.get('SubmissionStartDate') is not None:
            self.submission_start_date = m.get('SubmissionStartDate')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTransferInListResponseBodyDataTransferInInfo(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        email: str = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        instance_id: str = None,
        modification_date: str = None,
        modification_date_long: int = None,
        need_mail_check: bool = None,
        progress_bar_type: int = None,
        result_code: str = None,
        result_date: str = None,
        result_date_long: int = None,
        result_msg: str = None,
        simple_transfer_in_status: str = None,
        status: int = None,
        submission_date: str = None,
        submission_date_long: int = None,
        transfer_authorization_code_submission_date: str = None,
        transfer_authorization_code_submission_date_long: int = None,
        user_id: str = None,
        whois_mail_status: bool = None,
    ):
        self.domain_name = domain_name
        self.email = email
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.instance_id = instance_id
        self.modification_date = modification_date
        self.modification_date_long = modification_date_long
        self.need_mail_check = need_mail_check
        self.progress_bar_type = progress_bar_type
        self.result_code = result_code
        self.result_date = result_date
        self.result_date_long = result_date_long
        self.result_msg = result_msg
        self.simple_transfer_in_status = simple_transfer_in_status
        self.status = status
        self.submission_date = submission_date
        self.submission_date_long = submission_date_long
        self.transfer_authorization_code_submission_date = transfer_authorization_code_submission_date
        self.transfer_authorization_code_submission_date_long = transfer_authorization_code_submission_date_long
        self.user_id = user_id
        self.whois_mail_status = whois_mail_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date
        if self.modification_date_long is not None:
            result['ModificationDateLong'] = self.modification_date_long
        if self.need_mail_check is not None:
            result['NeedMailCheck'] = self.need_mail_check
        if self.progress_bar_type is not None:
            result['ProgressBarType'] = self.progress_bar_type
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_date is not None:
            result['ResultDate'] = self.result_date
        if self.result_date_long is not None:
            result['ResultDateLong'] = self.result_date_long
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        if self.submission_date_long is not None:
            result['SubmissionDateLong'] = self.submission_date_long
        if self.transfer_authorization_code_submission_date is not None:
            result['TransferAuthorizationCodeSubmissionDate'] = self.transfer_authorization_code_submission_date
        if self.transfer_authorization_code_submission_date_long is not None:
            result['TransferAuthorizationCodeSubmissionDateLong'] = self.transfer_authorization_code_submission_date_long
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.whois_mail_status is not None:
            result['WhoisMailStatus'] = self.whois_mail_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')
        if m.get('ModificationDateLong') is not None:
            self.modification_date_long = m.get('ModificationDateLong')
        if m.get('NeedMailCheck') is not None:
            self.need_mail_check = m.get('NeedMailCheck')
        if m.get('ProgressBarType') is not None:
            self.progress_bar_type = m.get('ProgressBarType')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultDate') is not None:
            self.result_date = m.get('ResultDate')
        if m.get('ResultDateLong') is not None:
            self.result_date_long = m.get('ResultDateLong')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        if m.get('SubmissionDateLong') is not None:
            self.submission_date_long = m.get('SubmissionDateLong')
        if m.get('TransferAuthorizationCodeSubmissionDate') is not None:
            self.transfer_authorization_code_submission_date = m.get('TransferAuthorizationCodeSubmissionDate')
        if m.get('TransferAuthorizationCodeSubmissionDateLong') is not None:
            self.transfer_authorization_code_submission_date_long = m.get('TransferAuthorizationCodeSubmissionDateLong')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WhoisMailStatus') is not None:
            self.whois_mail_status = m.get('WhoisMailStatus')
        return self


class QueryTransferInListResponseBodyData(TeaModel):
    def __init__(
        self,
        transfer_in_info: List[QueryTransferInListResponseBodyDataTransferInInfo] = None,
    ):
        self.transfer_in_info = transfer_in_info

    def validate(self):
        if self.transfer_in_info:
            for k in self.transfer_in_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TransferInInfo'] = []
        if self.transfer_in_info is not None:
            for k in self.transfer_in_info:
                result['TransferInInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.transfer_in_info = []
        if m.get('TransferInInfo') is not None:
            for k in m.get('TransferInInfo'):
                temp_model = QueryTransferInListResponseBodyDataTransferInInfo()
                self.transfer_in_info.append(temp_model.from_map(k))
        return self


class QueryTransferInListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTransferInListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTransferInListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTransferInListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTransferInListResponseBody = None,
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
            temp_model = QueryTransferInListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferOutInfoRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTransferOutInfoResponseBody(TeaModel):
    def __init__(
        self,
        email: str = None,
        expiration_date: str = None,
        pending_request_date: str = None,
        request_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        status: int = None,
        transfer_authorization_code_send_date: str = None,
    ):
        self.email = email
        self.expiration_date = expiration_date
        self.pending_request_date = pending_request_date
        self.request_id = request_id
        self.result_code = result_code
        self.result_msg = result_msg
        self.status = status
        self.transfer_authorization_code_send_date = transfer_authorization_code_send_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.pending_request_date is not None:
            result['PendingRequestDate'] = self.pending_request_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.status is not None:
            result['Status'] = self.status
        if self.transfer_authorization_code_send_date is not None:
            result['TransferAuthorizationCodeSendDate'] = self.transfer_authorization_code_send_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('PendingRequestDate') is not None:
            self.pending_request_date = m.get('PendingRequestDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransferAuthorizationCodeSendDate') is not None:
            self.transfer_authorization_code_send_date = m.get('TransferAuthorizationCodeSendDate')
        return self


class QueryTransferOutInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTransferOutInfoResponseBody = None,
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
            temp_model = QueryTransferOutInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegistrantProfileRealNameVerificationRequest(TeaModel):
    def __init__(
        self,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.identity_credential = identity_credential
        # This parameter is required.
        self.identity_credential_no = identity_credential_no
        # This parameter is required.
        self.identity_credential_type = identity_credential_type
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileID'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileID') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileID')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class RegistrantProfileRealNameVerificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegistrantProfileRealNameVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegistrantProfileRealNameVerificationResponseBody = None,
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
            temp_model = RegistrantProfileRealNameVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendEmailVerificationRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.email = email
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class ResendEmailVerificationResponseBodyFailList(TeaModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ResendEmailVerificationResponseBodySuccessList(TeaModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ResendEmailVerificationResponseBody(TeaModel):
    def __init__(
        self,
        fail_list: List[ResendEmailVerificationResponseBodyFailList] = None,
        request_id: str = None,
        success_list: List[ResendEmailVerificationResponseBodySuccessList] = None,
    ):
        self.fail_list = fail_list
        self.request_id = request_id
        self.success_list = success_list

    def validate(self):
        if self.fail_list:
            for k in self.fail_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailList'] = []
        if self.fail_list is not None:
            for k in self.fail_list:
                result['FailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_list = []
        if m.get('FailList') is not None:
            for k in m.get('FailList'):
                temp_model = ResendEmailVerificationResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = ResendEmailVerificationResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class ResendEmailVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResendEmailVerificationResponseBody = None,
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
            temp_model = ResendEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam(TeaModel):
    def __init__(
        self,
        address: str = None,
        aliyun_dns: bool = None,
        city: str = None,
        country: str = None,
        dns_1: str = None,
        dns_2: str = None,
        domain_name: str = None,
        email: str = None,
        enable_domain_proxy: bool = None,
        permit_premium_activation: bool = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_type: str = None,
        subscription_duration: int = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        trademark_domain_activation: bool = None,
    ):
        self.address = address
        self.aliyun_dns = aliyun_dns
        self.city = city
        self.country = country
        self.dns_1 = dns_1
        self.dns_2 = dns_2
        self.domain_name = domain_name
        self.email = email
        self.enable_domain_proxy = enable_domain_proxy
        self.permit_premium_activation = permit_premium_activation
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_profile_id = registrant_profile_id
        self.registrant_type = registrant_type
        self.subscription_duration = subscription_duration
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.trademark_domain_activation = trademark_domain_activation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1
        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_domain_proxy is not None:
            result['EnableDomainProxy'] = self.enable_domain_proxy
        if self.permit_premium_activation is not None:
            result['PermitPremiumActivation'] = self.permit_premium_activation
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.trademark_domain_activation is not None:
            result['TrademarkDomainActivation'] = self.trademark_domain_activation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')
        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableDomainProxy') is not None:
            self.enable_domain_proxy = m.get('EnableDomainProxy')
        if m.get('PermitPremiumActivation') is not None:
            self.permit_premium_activation = m.get('PermitPremiumActivation')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TrademarkDomainActivation') is not None:
            self.trademark_domain_activation = m.get('TrademarkDomainActivation')
        return self


class SaveBatchTaskForCreatingOrderActivateRequest(TeaModel):
    def __init__(
        self,
        coupon_no: str = None,
        lang: str = None,
        order_activate_param: List[SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam] = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        self.lang = lang
        # This parameter is required.
        self.order_activate_param = order_activate_param
        self.promotion_no = promotion_no
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.order_activate_param:
            for k in self.order_activate_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderActivateParam'] = []
        if self.order_activate_param is not None:
            for k in self.order_activate_param:
                result['OrderActivateParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_activate_param = []
        if m.get('OrderActivateParam') is not None:
            for k in m.get('OrderActivateParam'):
                temp_model = SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam()
                self.order_activate_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderActivateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderActivateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForCreatingOrderActivateResponseBody = None,
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
            temp_model = SaveBatchTaskForCreatingOrderActivateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderRedeemRequestOrderRedeemParam(TeaModel):
    def __init__(
        self,
        current_expiration_date: int = None,
        domain_name: str = None,
    ):
        self.current_expiration_date = current_expiration_date
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class SaveBatchTaskForCreatingOrderRedeemRequest(TeaModel):
    def __init__(
        self,
        coupon_no: str = None,
        lang: str = None,
        order_redeem_param: List[SaveBatchTaskForCreatingOrderRedeemRequestOrderRedeemParam] = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        self.lang = lang
        # This parameter is required.
        self.order_redeem_param = order_redeem_param
        self.promotion_no = promotion_no
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.order_redeem_param:
            for k in self.order_redeem_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderRedeemParam'] = []
        if self.order_redeem_param is not None:
            for k in self.order_redeem_param:
                result['OrderRedeemParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_redeem_param = []
        if m.get('OrderRedeemParam') is not None:
            for k in m.get('OrderRedeemParam'):
                temp_model = SaveBatchTaskForCreatingOrderRedeemRequestOrderRedeemParam()
                self.order_redeem_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderRedeemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderRedeemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForCreatingOrderRedeemResponseBody = None,
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
            temp_model = SaveBatchTaskForCreatingOrderRedeemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam(TeaModel):
    def __init__(
        self,
        current_expiration_date: int = None,
        domain_name: str = None,
        subscription_duration: int = None,
    ):
        self.current_expiration_date = current_expiration_date
        self.domain_name = domain_name
        self.subscription_duration = subscription_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        return self


class SaveBatchTaskForCreatingOrderRenewRequest(TeaModel):
    def __init__(
        self,
        coupon_no: str = None,
        lang: str = None,
        order_renew_param: List[SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam] = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        self.lang = lang
        # This parameter is required.
        self.order_renew_param = order_renew_param
        self.promotion_no = promotion_no
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.order_renew_param:
            for k in self.order_renew_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderRenewParam'] = []
        if self.order_renew_param is not None:
            for k in self.order_renew_param:
                result['OrderRenewParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_renew_param = []
        if m.get('OrderRenewParam') is not None:
            for k in m.get('OrderRenewParam'):
                temp_model = SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam()
                self.order_renew_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderRenewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderRenewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForCreatingOrderRenewResponseBody = None,
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
            temp_model = SaveBatchTaskForCreatingOrderRenewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam(TeaModel):
    def __init__(
        self,
        authorization_code: str = None,
        domain_name: str = None,
        permit_premium_transfer: bool = None,
        registrant_profile_id: int = None,
    ):
        self.authorization_code = authorization_code
        self.domain_name = domain_name
        self.permit_premium_transfer = permit_premium_transfer
        self.registrant_profile_id = registrant_profile_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.permit_premium_transfer is not None:
            result['PermitPremiumTransfer'] = self.permit_premium_transfer
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PermitPremiumTransfer') is not None:
            self.permit_premium_transfer = m.get('PermitPremiumTransfer')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        return self


class SaveBatchTaskForCreatingOrderTransferRequest(TeaModel):
    def __init__(
        self,
        coupon_no: str = None,
        lang: str = None,
        order_transfer_param: List[SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam] = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        self.lang = lang
        # This parameter is required.
        self.order_transfer_param = order_transfer_param
        self.promotion_no = promotion_no
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        if self.order_transfer_param:
            for k in self.order_transfer_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderTransferParam'] = []
        if self.order_transfer_param is not None:
            for k in self.order_transfer_param:
                result['OrderTransferParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_transfer_param = []
        if m.get('OrderTransferParam') is not None:
            for k in m.get('OrderTransferParam'):
                temp_model = SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam()
                self.order_transfer_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderTransferResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderTransferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForCreatingOrderTransferResponseBody = None,
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
            temp_model = SaveBatchTaskForCreatingOrderTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForDomainNameProxyServiceRequest(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
        status: bool = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SaveBatchTaskForDomainNameProxyServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForDomainNameProxyServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForDomainNameProxyServiceResponseBody = None,
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
            temp_model = SaveBatchTaskForDomainNameProxyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForModifyingDomainDnsRequest(TeaModel):
    def __init__(
        self,
        aliyun_dns: bool = None,
        domain_name: List[str] = None,
        domain_name_server: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.aliyun_dns = aliyun_dns
        # This parameter is required.
        self.domain_name = domain_name
        self.domain_name_server = domain_name_server
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_server is not None:
            result['DomainNameServer'] = self.domain_name_server
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameServer') is not None:
            self.domain_name_server = m.get('DomainNameServer')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForModifyingDomainDnsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForModifyingDomainDnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForModifyingDomainDnsResponseBody = None,
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
            temp_model = SaveBatchTaskForModifyingDomainDnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForReserveDropListDomainRequestDomains(TeaModel):
    def __init__(
        self,
        dns_1: str = None,
        dns_2: str = None,
        domain_name: str = None,
    ):
        self.dns_1 = dns_1
        self.dns_2 = dns_2
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1
        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')
        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class SaveBatchTaskForReserveDropListDomainRequest(TeaModel):
    def __init__(
        self,
        contact_template_id: str = None,
        domains: List[SaveBatchTaskForReserveDropListDomainRequestDomains] = None,
    ):
        # This parameter is required.
        self.contact_template_id = contact_template_id
        # This parameter is required.
        self.domains = domains

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = SaveBatchTaskForReserveDropListDomainRequestDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class SaveBatchTaskForReserveDropListDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForReserveDropListDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForReserveDropListDomainResponseBody = None,
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
            temp_model = SaveBatchTaskForReserveDropListDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForTransferProhibitionLockRequest(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        lang: str = None,
        status: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.status = status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForTransferProhibitionLockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForTransferProhibitionLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForTransferProhibitionLockResponseBody = None,
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
            temp_model = SaveBatchTaskForTransferProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForUpdateProhibitionLockRequest(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        lang: str = None,
        status: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.status = status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForUpdateProhibitionLockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForUpdateProhibitionLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForUpdateProhibitionLockResponseBody = None,
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
            temp_model = SaveBatchTaskForUpdateProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForUpdatingContactInfoRequest(TeaModel):
    def __init__(
        self,
        add_transfer_lock: bool = None,
        contact_type: str = None,
        domain_name: List[str] = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        self.add_transfer_lock = add_transfer_lock
        # This parameter is required.
        self.contact_type = contact_type
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_transfer_lock is not None:
            result['AddTransferLock'] = self.add_transfer_lock
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTransferLock') is not None:
            self.add_transfer_lock = m.get('AddTransferLock')
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForUpdatingContactInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForUpdatingContactInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForUpdatingContactInfoResponseBody = None,
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
            temp_model = SaveBatchTaskForUpdatingContactInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForUpdatingContactInfoByNewContactRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        contact_type: str = None,
        country: str = None,
        domain_name: List[str] = None,
        email: str = None,
        lang: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        transfer_out_prohibited: bool = None,
        user_client_ip: str = None,
    ):
        self.address = address
        self.city = city
        # This parameter is required.
        self.contact_type = contact_type
        self.country = country
        # This parameter is required.
        self.domain_name = domain_name
        self.email = email
        self.lang = lang
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.transfer_out_prohibited = transfer_out_prohibited
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.country is not None:
            result['Country'] = self.country
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForUpdatingContactInfoByNewContactResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForUpdatingContactInfoByNewContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveBatchTaskForUpdatingContactInfoByNewContactResponseBody = None,
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
            temp_model = SaveBatchTaskForUpdatingContactInfoByNewContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveRegistrantProfileRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        default_registrant_profile: bool = None,
        email: str = None,
        lang: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_profile_type: str = None,
        registrant_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        user_client_ip: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        self.default_registrant_profile = default_registrant_profile
        self.email = email
        self.lang = lang
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_profile_id = registrant_profile_id
        self.registrant_profile_type = registrant_profile_type
        self.registrant_type = registrant_type
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveRegistrantProfileResponseBody(TeaModel):
    def __init__(
        self,
        registrant_profile_id: int = None,
        request_id: str = None,
    ):
        self.registrant_profile_id = registrant_profile_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveRegistrantProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveRegistrantProfileResponseBody = None,
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
            temp_model = SaveRegistrantProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForAddingDSRecordRequest(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        digest: str = None,
        digest_type: int = None,
        domain_name: str = None,
        key_tag: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.algorithm = algorithm
        # This parameter is required.
        self.digest = digest
        # This parameter is required.
        self.digest_type = digest_type
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.key_tag = key_tag
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_type is not None:
            result['DigestType'] = self.digest_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForAddingDSRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForAddingDSRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForAddingDSRecordResponseBody = None,
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
            temp_model = SaveSingleTaskForAddingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForApprovingTransferOutRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForApprovingTransferOutResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForApprovingTransferOutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForApprovingTransferOutResponseBody = None,
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
            temp_model = SaveSingleTaskForApprovingTransferOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForAssociatingEnsRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.address = address
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForAssociatingEnsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForAssociatingEnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForAssociatingEnsResponseBody = None,
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
            temp_model = SaveSingleTaskForAssociatingEnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCancelingTransferInRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCancelingTransferInResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCancelingTransferInResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForCancelingTransferInResponseBody = None,
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
            temp_model = SaveSingleTaskForCancelingTransferInResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCancelingTransferOutRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCancelingTransferOutResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCancelingTransferOutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForCancelingTransferOutResponseBody = None,
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
            temp_model = SaveSingleTaskForCancelingTransferOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingDnsHostRequest(TeaModel):
    def __init__(
        self,
        dns_name: str = None,
        instance_id: str = None,
        ip: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.dns_name = dns_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.ip = ip
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingDnsHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingDnsHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForCreatingDnsHostResponseBody = None,
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
            temp_model = SaveSingleTaskForCreatingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderActivateRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        aliyun_dns: bool = None,
        city: str = None,
        country: str = None,
        coupon_no: str = None,
        dns_1: str = None,
        dns_2: str = None,
        domain_name: str = None,
        email: str = None,
        enable_domain_proxy: bool = None,
        lang: str = None,
        permit_premium_activation: bool = None,
        postal_code: str = None,
        promotion_no: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_type: str = None,
        subscription_duration: int = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        trademark_domain_activation: bool = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.address = address
        self.aliyun_dns = aliyun_dns
        self.city = city
        self.country = country
        self.coupon_no = coupon_no
        self.dns_1 = dns_1
        self.dns_2 = dns_2
        # This parameter is required.
        self.domain_name = domain_name
        self.email = email
        self.enable_domain_proxy = enable_domain_proxy
        self.lang = lang
        self.permit_premium_activation = permit_premium_activation
        self.postal_code = postal_code
        self.promotion_no = promotion_no
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_profile_id = registrant_profile_id
        self.registrant_type = registrant_type
        self.subscription_duration = subscription_duration
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.trademark_domain_activation = trademark_domain_activation
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1
        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_domain_proxy is not None:
            result['EnableDomainProxy'] = self.enable_domain_proxy
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.permit_premium_activation is not None:
            result['PermitPremiumActivation'] = self.permit_premium_activation
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.trademark_domain_activation is not None:
            result['TrademarkDomainActivation'] = self.trademark_domain_activation
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')
        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableDomainProxy') is not None:
            self.enable_domain_proxy = m.get('EnableDomainProxy')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PermitPremiumActivation') is not None:
            self.permit_premium_activation = m.get('PermitPremiumActivation')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TrademarkDomainActivation') is not None:
            self.trademark_domain_activation = m.get('TrademarkDomainActivation')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderActivateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderActivateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForCreatingOrderActivateResponseBody = None,
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
            temp_model = SaveSingleTaskForCreatingOrderActivateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderRedeemRequest(TeaModel):
    def __init__(
        self,
        coupon_no: str = None,
        current_expiration_date: int = None,
        domain_name: str = None,
        lang: str = None,
        promotion_no: str = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        # This parameter is required.
        self.current_expiration_date = current_expiration_date
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.promotion_no = promotion_no
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderRedeemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderRedeemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForCreatingOrderRedeemResponseBody = None,
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
            temp_model = SaveSingleTaskForCreatingOrderRedeemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderRenewRequest(TeaModel):
    def __init__(
        self,
        coupon_no: str = None,
        current_expiration_date: int = None,
        domain_name: str = None,
        lang: str = None,
        promotion_no: str = None,
        subscription_duration: int = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        self.coupon_no = coupon_no
        # This parameter is required.
        self.current_expiration_date = current_expiration_date
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.promotion_no = promotion_no
        # This parameter is required.
        self.subscription_duration = subscription_duration
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderRenewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderRenewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForCreatingOrderRenewResponseBody = None,
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
            temp_model = SaveSingleTaskForCreatingOrderRenewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderTransferRequest(TeaModel):
    def __init__(
        self,
        authorization_code: str = None,
        coupon_no: str = None,
        domain_name: str = None,
        lang: str = None,
        permit_premium_transfer: bool = None,
        promotion_no: str = None,
        registrant_profile_id: int = None,
        use_coupon: bool = None,
        use_promotion: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.authorization_code = authorization_code
        self.coupon_no = coupon_no
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.permit_premium_transfer = permit_premium_transfer
        self.promotion_no = promotion_no
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.use_coupon = use_coupon
        self.use_promotion = use_promotion
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.permit_premium_transfer is not None:
            result['PermitPremiumTransfer'] = self.permit_premium_transfer
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PermitPremiumTransfer') is not None:
            self.permit_premium_transfer = m.get('PermitPremiumTransfer')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderTransferResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderTransferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForCreatingOrderTransferResponseBody = None,
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
            temp_model = SaveSingleTaskForCreatingOrderTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDeletingDSRecordRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        key_tag: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.key_tag = key_tag
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDeletingDSRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDeletingDSRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForDeletingDSRecordResponseBody = None,
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
            temp_model = SaveSingleTaskForDeletingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDeletingDnsHostRequest(TeaModel):
    def __init__(
        self,
        dns_name: str = None,
        instance_id: str = None,
        ip: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.dns_name = dns_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.ip = ip
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDeletingDnsHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDeletingDnsHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForDeletingDnsHostResponseBody = None,
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
            temp_model = SaveSingleTaskForDeletingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDisassociatingEnsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDisassociatingEnsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDisassociatingEnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForDisassociatingEnsResponseBody = None,
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
            temp_model = SaveSingleTaskForDisassociatingEnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDomainNameProxyServiceRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        status: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.status = status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDomainNameProxyServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDomainNameProxyServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForDomainNameProxyServiceResponseBody = None,
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
            temp_model = SaveSingleTaskForDomainNameProxyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForModifyingDSRecordRequest(TeaModel):
    def __init__(
        self,
        algorithm: int = None,
        digest: str = None,
        digest_type: int = None,
        domain_name: str = None,
        key_tag: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.algorithm = algorithm
        # This parameter is required.
        self.digest = digest
        # This parameter is required.
        self.digest_type = digest_type
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.key_tag = key_tag
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_type is not None:
            result['DigestType'] = self.digest_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForModifyingDSRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForModifyingDSRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForModifyingDSRecordResponseBody = None,
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
            temp_model = SaveSingleTaskForModifyingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForModifyingDnsHostRequest(TeaModel):
    def __init__(
        self,
        dns_name: str = None,
        instance_id: str = None,
        ip: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.dns_name = dns_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.ip = ip
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForModifyingDnsHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForModifyingDnsHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForModifyingDnsHostResponseBody = None,
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
            temp_model = SaveSingleTaskForModifyingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForQueryingTransferAuthorizationCodeRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForQueryingTransferAuthorizationCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForQueryingTransferAuthorizationCodeResponseBody = None,
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
            temp_model = SaveSingleTaskForQueryingTransferAuthorizationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForSaveArtExtensionRequest(TeaModel):
    def __init__(
        self,
        date_or_period: str = None,
        dimensions: str = None,
        domain_name: str = None,
        features: str = None,
        inscriptions_and_markings: str = None,
        lang: str = None,
        maker: str = None,
        materials_and_techniques: str = None,
        object_type: str = None,
        reference: str = None,
        subject: str = None,
        title: str = None,
    ):
        self.date_or_period = date_or_period
        self.dimensions = dimensions
        # This parameter is required.
        self.domain_name = domain_name
        self.features = features
        self.inscriptions_and_markings = inscriptions_and_markings
        self.lang = lang
        self.maker = maker
        self.materials_and_techniques = materials_and_techniques
        self.object_type = object_type
        self.reference = reference
        self.subject = subject
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_or_period is not None:
            result['DateOrPeriod'] = self.date_or_period
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.features is not None:
            result['Features'] = self.features
        if self.inscriptions_and_markings is not None:
            result['InscriptionsAndMarkings'] = self.inscriptions_and_markings
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.maker is not None:
            result['Maker'] = self.maker
        if self.materials_and_techniques is not None:
            result['MaterialsAndTechniques'] = self.materials_and_techniques
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.reference is not None:
            result['Reference'] = self.reference
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateOrPeriod') is not None:
            self.date_or_period = m.get('DateOrPeriod')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InscriptionsAndMarkings') is not None:
            self.inscriptions_and_markings = m.get('InscriptionsAndMarkings')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Maker') is not None:
            self.maker = m.get('Maker')
        if m.get('MaterialsAndTechniques') is not None:
            self.materials_and_techniques = m.get('MaterialsAndTechniques')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SaveSingleTaskForSaveArtExtensionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForSaveArtExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForSaveArtExtensionResponseBody = None,
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
            temp_model = SaveSingleTaskForSaveArtExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForSynchronizingDSRecordRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForSynchronizingDSRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForSynchronizingDSRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForSynchronizingDSRecordResponseBody = None,
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
            temp_model = SaveSingleTaskForSynchronizingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForSynchronizingDnsHostRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForSynchronizingDnsHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForSynchronizingDnsHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForSynchronizingDnsHostResponseBody = None,
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
            temp_model = SaveSingleTaskForSynchronizingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForTransferProhibitionLockRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        status: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.status = status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForTransferProhibitionLockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForTransferProhibitionLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForTransferProhibitionLockResponseBody = None,
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
            temp_model = SaveSingleTaskForTransferProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForUpdateProhibitionLockRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        status: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.status = status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForUpdateProhibitionLockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForUpdateProhibitionLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForUpdateProhibitionLockResponseBody = None,
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
            temp_model = SaveSingleTaskForUpdateProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForUpdatingContactInfoRequest(TeaModel):
    def __init__(
        self,
        add_transfer_lock: bool = None,
        contact_type: str = None,
        domain_name: str = None,
        instance_id: str = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        self.add_transfer_lock = add_transfer_lock
        # This parameter is required.
        self.contact_type = contact_type
        # This parameter is required.
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_transfer_lock is not None:
            result['AddTransferLock'] = self.add_transfer_lock
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTransferLock') is not None:
            self.add_transfer_lock = m.get('AddTransferLock')
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForUpdatingContactInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForUpdatingContactInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSingleTaskForUpdatingContactInfoResponseBody = None,
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
            temp_model = SaveSingleTaskForUpdatingContactInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForSubmittingDomainDeleteRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForSubmittingDomainDeleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForSubmittingDomainDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTaskForSubmittingDomainDeleteResponseBody = None,
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
            temp_model = SaveTaskForSubmittingDomainDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.identity_credential = identity_credential
        # This parameter is required.
        self.identity_credential_no = identity_credential_no
        # This parameter is required.
        self.identity_credential_type = identity_credential_type
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponseBody = None,
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
            temp_model = SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        instance_id: str = None,
        lang: str = None,
        registrant_profile_id: int = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponseBody = None,
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
            temp_model = SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        domain_name: List[str] = None,
        email: str = None,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        lang: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        transfer_out_prohibited: bool = None,
        user_client_ip: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        # This parameter is required.
        self.domain_name = domain_name
        self.email = email
        # This parameter is required.
        self.identity_credential = identity_credential
        # This parameter is required.
        self.identity_credential_no = identity_credential_no
        # This parameter is required.
        self.identity_credential_type = identity_credential_type
        self.lang = lang
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        # This parameter is required.
        self.registrant_type = registrant_type
        # This parameter is required.
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        # This parameter is required.
        self.telephone = telephone
        # This parameter is required.
        self.transfer_out_prohibited = transfer_out_prohibited
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponseBody = None,
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
            temp_model = SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        lang: str = None,
        registrant_profile_id: int = None,
        transfer_out_prohibited: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.registrant_profile_id = registrant_profile_id
        # This parameter is required.
        self.transfer_out_prohibited = transfer_out_prohibited
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponseBody = None,
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
            temp_model = SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitEmailVerificationRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        lang: str = None,
        send_if_exist: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.email = email
        self.lang = lang
        self.send_if_exist = send_if_exist
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.send_if_exist is not None:
            result['SendIfExist'] = self.send_if_exist
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SendIfExist') is not None:
            self.send_if_exist = m.get('SendIfExist')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SubmitEmailVerificationResponseBodyExistList(TeaModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitEmailVerificationResponseBodyFailList(TeaModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitEmailVerificationResponseBodySuccessList(TeaModel):
    def __init__(
        self,
        code: str = None,
        email: str = None,
        message: str = None,
    ):
        self.code = code
        self.email = email
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitEmailVerificationResponseBody(TeaModel):
    def __init__(
        self,
        exist_list: List[SubmitEmailVerificationResponseBodyExistList] = None,
        fail_list: List[SubmitEmailVerificationResponseBodyFailList] = None,
        request_id: str = None,
        success_list: List[SubmitEmailVerificationResponseBodySuccessList] = None,
    ):
        self.exist_list = exist_list
        self.fail_list = fail_list
        self.request_id = request_id
        self.success_list = success_list

    def validate(self):
        if self.exist_list:
            for k in self.exist_list:
                if k:
                    k.validate()
        if self.fail_list:
            for k in self.fail_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExistList'] = []
        if self.exist_list is not None:
            for k in self.exist_list:
                result['ExistList'].append(k.to_map() if k else None)
        result['FailList'] = []
        if self.fail_list is not None:
            for k in self.fail_list:
                result['FailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exist_list = []
        if m.get('ExistList') is not None:
            for k in m.get('ExistList'):
                temp_model = SubmitEmailVerificationResponseBodyExistList()
                self.exist_list.append(temp_model.from_map(k))
        self.fail_list = []
        if m.get('FailList') is not None:
            for k in m.get('FailList'):
                temp_model = SubmitEmailVerificationResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = SubmitEmailVerificationResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class SubmitEmailVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitEmailVerificationResponseBody = None,
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
            temp_model = SubmitEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInCheckMailTokenRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        token: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.token = token
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.token is not None:
            result['Token'] = self.token
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInCheckMailTokenResponseBodyFailList(TeaModel):
    def __init__(
        self,
        fail_domain: List[str] = None,
    ):
        self.fail_domain = fail_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_domain is not None:
            result['FailDomain'] = self.fail_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailDomain') is not None:
            self.fail_domain = m.get('FailDomain')
        return self


class TransferInCheckMailTokenResponseBodySuccessList(TeaModel):
    def __init__(
        self,
        success_domain: List[str] = None,
    ):
        self.success_domain = success_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_domain is not None:
            result['SuccessDomain'] = self.success_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccessDomain') is not None:
            self.success_domain = m.get('SuccessDomain')
        return self


class TransferInCheckMailTokenResponseBody(TeaModel):
    def __init__(
        self,
        fail_list: TransferInCheckMailTokenResponseBodyFailList = None,
        request_id: str = None,
        success_list: TransferInCheckMailTokenResponseBodySuccessList = None,
    ):
        self.fail_list = fail_list
        self.request_id = request_id
        self.success_list = success_list

    def validate(self):
        if self.fail_list:
            self.fail_list.validate()
        if self.success_list:
            self.success_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_list is not None:
            result['FailList'] = self.fail_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_list is not None:
            result['SuccessList'] = self.success_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailList') is not None:
            temp_model = TransferInCheckMailTokenResponseBodyFailList()
            self.fail_list = temp_model.from_map(m['FailList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessList') is not None:
            temp_model = TransferInCheckMailTokenResponseBodySuccessList()
            self.success_list = temp_model.from_map(m['SuccessList'])
        return self


class TransferInCheckMailTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferInCheckMailTokenResponseBody = None,
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
            temp_model = TransferInCheckMailTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInReenterTransferAuthorizationCodeRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        transfer_authorization_code: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.transfer_authorization_code = transfer_authorization_code
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.transfer_authorization_code is not None:
            result['TransferAuthorizationCode'] = self.transfer_authorization_code
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TransferAuthorizationCode') is not None:
            self.transfer_authorization_code = m.get('TransferAuthorizationCode')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInReenterTransferAuthorizationCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransferInReenterTransferAuthorizationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferInReenterTransferAuthorizationCodeResponseBody = None,
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
            temp_model = TransferInReenterTransferAuthorizationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInRefetchWhoisEmailRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInRefetchWhoisEmailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransferInRefetchWhoisEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferInRefetchWhoisEmailResponseBody = None,
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
            temp_model = TransferInRefetchWhoisEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInResendMailTokenRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInResendMailTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransferInResendMailTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferInResendMailTokenResponseBody = None,
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
            temp_model = TransferInResendMailTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyContactFieldRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        domain_name: str = None,
        email: str = None,
        lang: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        user_client_ip: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        self.domain_name = domain_name
        self.email = email
        self.lang = lang
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_type = registrant_type
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class VerifyContactFieldResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyContactFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyContactFieldResponseBody = None,
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
            temp_model = VerifyContactFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyEmailRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        token: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.token = token
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.token is not None:
            result['Token'] = self.token
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class VerifyEmailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyEmailResponseBody = None,
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
            temp_model = VerifyEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


