# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTransferInByInstanceIdResponseBody(DaraModel):
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
        # Domain name.
        self.domain_name = domain_name
        # Mailbox to which the domain name transfer-in confirmation email was sent.
        self.email = email
        # The expiration time of the domain name transfer-in.
        self.expiration_date = expiration_date
        # The UNIX timestamp indicating when the transfer-in expires.
        self.expiration_date_long = expiration_date_long
        # Instance ID.
        self.instance_id = instance_id
        # The update time of the transfer-in information.
        self.modification_date = modification_date
        # The UNIX timestamp indicating when the transfer-in information was updated.
        self.modification_date_long = modification_date_long
        # Indicates whether email verification is required.
        self.need_mail_check = need_mail_check
        # Progress bar chart type for the transfer procedure. Valid values:  
        # - **0**: Both email verification and naming review are required;  
        # - **1**: Email verification is required, but naming review is not;  
        # - **2**: Naming review is required, but email verification is not;  
        # - **3**: Neither email verification nor naming review is required.
        self.progress_bar_type = progress_bar_type
        # Unique request access token.
        self.request_id = request_id
        # The error code indicating the reason for transfer failure. Valid values:
        # - **clientCancelled**: You canceled the domain transfer-in.
        # - **clientRejected**: The original registrar rejected the domain transfer-in (or you performed a rejection operation through the original registrar).
        # - **serverCancelled**: The domain name registry canceled the transfer.
        # - **transferProhibited**: The domain is in a transfer-prohibited status.
        # - **transferExpired**: You did not complete the required transfer confirmation within the validity period.
        # - **nameVerificationFailed**: The domain naming review did not pass.
        # - **transferSubmitted**: Another user has already submitted a transfer request for this domain.
        self.result_code = result_code
        # The time when the transfer succeeded or failed.
        self.result_date = result_date
        # The UNIX timestamp indicating when the transfer succeeded or failed.
        self.result_date_long = result_date_long
        # Description of the failure reason when the transfer failed.
        self.result_msg = result_msg
        # Transfer status. Valid values:  
        # - **INIT**: Transfer-in submitted;  
        # - **AUTHORIZATION**: Authorization for transfer-in (email verification);  
        # - **NAME_VERIFICATION**: Naming review;  
        # - **PASSWORD_VERIFICATION**: Transfer password verification;  
        # - **PENDING**: Transfer-in in progress;  
        # - **SUCCESS**: Transfer-in succeeded;  
        # - **FAIL**: Transfer-in failed.
        self.simple_transfer_in_status = simple_transfer_in_status
        # Detailed domain name transfer-in status. Valid values:  
        # - **10**: Initial status;  
        # - **11**: Email verification token link has been sent;  
        # - **19**: Token link has been successfully verified;  
        # - **20**: Naming review has been submitted;  
        # - **21**: Naming review failed;  
        # - **29**: Naming review succeeded;  
        # - **31**: Transfer password is incorrect;  
        # - **39**: Transfer-in submission succeeded;  
        # - **50**: Customer canceled the transfer-in;  
        # - **51**: Transfer-in failed;  
        # - **52**: Transfer-in expired;  
        # - **59**: Transfer-in succeeded.
        self.status = status
        # Transfer request submission time.
        self.submission_date = submission_date
        # UNIX timestamp of the transfer request submission time.
        self.submission_date_long = submission_date_long
        # Time when the transfer password was successfully submitted.
        self.transfer_authorization_code_submission_date = transfer_authorization_code_submission_date
        # UNIX timestamp of the time when the transfer password was successfully submitted.
        self.transfer_authorization_code_submission_date_long = transfer_authorization_code_submission_date_long
        # User ID.
        self.user_id = user_id
        # Indicates whether the registrant\\"s mailbox was scraped from WHOIS. When the domain transfer-in is in the authorization (email verification) phase and this field is **false**, it means the registrant\\"s mailbox was not obtained via WHOIS scraping, and manual processing is required.
        self.whois_mail_status = whois_mail_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

