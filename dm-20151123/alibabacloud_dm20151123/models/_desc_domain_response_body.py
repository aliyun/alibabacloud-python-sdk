# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescDomainResponseBody(DaraModel):
    def __init__(
        self,
        cname_auth_status: str = None,
        cname_confirm_status: str = None,
        cname_record: str = None,
        create_time: str = None,
        default_domain: str = None,
        dkim_auth_status: str = None,
        dkim_public_key: str = None,
        dkim_rr: str = None,
        dkim_rsa_length: int = None,
        dmarc_auth_status: int = None,
        dmarc_host_record: str = None,
        dmarc_record: str = None,
        dns_dmarc: str = None,
        dns_mx: str = None,
        dns_spf: str = None,
        dns_txt: str = None,
        domain_id: str = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_type: str = None,
        host_record: str = None,
        icp_status: str = None,
        mx_auth_status: str = None,
        mx_record: str = None,
        request_id: str = None,
        spf_auth_status: str = None,
        spf_record: str = None,
        spf_record_v2: str = None,
        tl_domain_name: str = None,
        tracef_record: str = None,
    ):
        # CNAME verification flag, 0 for success, 1 for failure.
        self.cname_auth_status = cname_auth_status
        # Indicates whether the CNAME host record has been modified, 1 for modified (reverting to the original value also counts as modification), 0 for not modified.
        self.cname_confirm_status = cname_confirm_status
        # Custom part of the CNAME host record
        self.cname_record = cname_record
        # Creation time
        self.create_time = create_time
        # Whether it is the default domain,
        # 
        # Value: 0 No (this field is deprecated)
        self.default_domain = default_domain
        # DKIM verification flag, indicating whether the DKIM record set by the user in DNS has passed validation, 0: Passed, 1: Not passed
        self.dkim_auth_status = dkim_auth_status
        # DKIM public key value, the value that users need to set for the DKIM record in DNS
        self.dkim_public_key = dkim_public_key
        # DKIM host record, the key that the user needs to set in the DNS for the DKIM record
        self.dkim_rr = dkim_rr
        self.dkim_rsa_length = dkim_rsa_length
        # DMARC verification flag, indicating whether the DMARC record set by the user in DNS has passed validation, 0: Passed, 1: Not passed
        self.dmarc_auth_status = dmarc_auth_status
        # DMARC host record value
        self.dmarc_host_record = dmarc_host_record
        # DMARC record value
        self.dmarc_record = dmarc_record
        # DMARC record value resolved through the public domain name
        self.dns_dmarc = dns_dmarc
        # MX record value resolved from the public network domain
        self.dns_mx = dns_mx
        # SPF record value resolved from the public network domain
        self.dns_spf = dns_spf
        # Ownership record value resolved from the public network domain
        self.dns_txt = dns_txt
        # Domain ID
        self.domain_id = domain_id
        # Domain name
        self.domain_name = domain_name
        # Domain status. Indicates whether the verification was successful, with values:
        # 
        # - **0**: Available, verified successfully
        # - **1**: Unavailable, verification failed
        self.domain_status = domain_status
        # Ownership record provided by the email push console
        self.domain_type = domain_type
        # Host record
        self.host_record = host_record
        # Filing status. **1** indicates filed, **0** indicates not filed.
        self.icp_status = icp_status
        # MX verification flag, 0 for success, 1 for failure.
        self.mx_auth_status = mx_auth_status
        # MX record value provided by the email push console
        self.mx_record = mx_record
        # Request ID
        self.request_id = request_id
        # SPF verification flag, 0 for success, 1 for failure.
        self.spf_auth_status = spf_auth_status
        # SPF record value provided by the email push console
        self.spf_record = spf_record
        # SPF record. Previously, the SPF display content needed to be calculated by the calling end based on the spfRecord in the response. The new field spfRecordV2 replaces spfRecord, and the calling end can directly display this field after obtaining it;
        self.spf_record_v2 = spf_record_v2
        # Primary domain
        self.tl_domain_name = tl_domain_name
        # CNAME record value provided by the email push console
        self.tracef_record = tracef_record

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status

        if self.cname_confirm_status is not None:
            result['CnameConfirmStatus'] = self.cname_confirm_status

        if self.cname_record is not None:
            result['CnameRecord'] = self.cname_record

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain

        if self.dkim_auth_status is not None:
            result['DkimAuthStatus'] = self.dkim_auth_status

        if self.dkim_public_key is not None:
            result['DkimPublicKey'] = self.dkim_public_key

        if self.dkim_rr is not None:
            result['DkimRR'] = self.dkim_rr

        if self.dkim_rsa_length is not None:
            result['DkimRsaLength'] = self.dkim_rsa_length

        if self.dmarc_auth_status is not None:
            result['DmarcAuthStatus'] = self.dmarc_auth_status

        if self.dmarc_host_record is not None:
            result['DmarcHostRecord'] = self.dmarc_host_record

        if self.dmarc_record is not None:
            result['DmarcRecord'] = self.dmarc_record

        if self.dns_dmarc is not None:
            result['DnsDmarc'] = self.dns_dmarc

        if self.dns_mx is not None:
            result['DnsMx'] = self.dns_mx

        if self.dns_spf is not None:
            result['DnsSpf'] = self.dns_spf

        if self.dns_txt is not None:
            result['DnsTxt'] = self.dns_txt

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.host_record is not None:
            result['HostRecord'] = self.host_record

        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status

        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status

        if self.mx_record is not None:
            result['MxRecord'] = self.mx_record

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status

        if self.spf_record is not None:
            result['SpfRecord'] = self.spf_record

        if self.spf_record_v2 is not None:
            result['SpfRecordV2'] = self.spf_record_v2

        if self.tl_domain_name is not None:
            result['TlDomainName'] = self.tl_domain_name

        if self.tracef_record is not None:
            result['TracefRecord'] = self.tracef_record

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')

        if m.get('CnameConfirmStatus') is not None:
            self.cname_confirm_status = m.get('CnameConfirmStatus')

        if m.get('CnameRecord') is not None:
            self.cname_record = m.get('CnameRecord')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')

        if m.get('DkimAuthStatus') is not None:
            self.dkim_auth_status = m.get('DkimAuthStatus')

        if m.get('DkimPublicKey') is not None:
            self.dkim_public_key = m.get('DkimPublicKey')

        if m.get('DkimRR') is not None:
            self.dkim_rr = m.get('DkimRR')

        if m.get('DkimRsaLength') is not None:
            self.dkim_rsa_length = m.get('DkimRsaLength')

        if m.get('DmarcAuthStatus') is not None:
            self.dmarc_auth_status = m.get('DmarcAuthStatus')

        if m.get('DmarcHostRecord') is not None:
            self.dmarc_host_record = m.get('DmarcHostRecord')

        if m.get('DmarcRecord') is not None:
            self.dmarc_record = m.get('DmarcRecord')

        if m.get('DnsDmarc') is not None:
            self.dns_dmarc = m.get('DnsDmarc')

        if m.get('DnsMx') is not None:
            self.dns_mx = m.get('DnsMx')

        if m.get('DnsSpf') is not None:
            self.dns_spf = m.get('DnsSpf')

        if m.get('DnsTxt') is not None:
            self.dns_txt = m.get('DnsTxt')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('HostRecord') is not None:
            self.host_record = m.get('HostRecord')

        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')

        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')

        if m.get('MxRecord') is not None:
            self.mx_record = m.get('MxRecord')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')

        if m.get('SpfRecord') is not None:
            self.spf_record = m.get('SpfRecord')

        if m.get('SpfRecordV2') is not None:
            self.spf_record_v2 = m.get('SpfRecordV2')

        if m.get('TlDomainName') is not None:
            self.tl_domain_name = m.get('TlDomainName')

        if m.get('TracefRecord') is not None:
            self.tracef_record = m.get('TracefRecord')

        return self

