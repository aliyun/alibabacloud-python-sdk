2025-06-27 Version: 1.1.2
- Update API DescribeCACertificateList: add response parameters Body.CertificateList.$.Gift.
- Update API DescribeCACertificateList: add response parameters Body.CertificateList.$.Trial.


2025-06-19 Version: 1.1.1
- Update API DescribeCACertificateList: add response parameters Body.CertificateList.$.Alias.


2025-06-18 Version: 1.1.0
- Support API ListCert.
- Support API UploadPcaCertToCas.
- Update API DescribeCACertificateList: add request parameters CaStatus.
- Update API DescribeCACertificateList: add request parameters CertType.
- Update API DescribeCACertificateList: add request parameters IssuerType.
- Update API DescribeCACertificateList: add request parameters ValidStatus.


2025-03-27 Version: 1.0.17
- Update API CreateClientCertificateWithCsr: add response parameters Body.CertKmcRep1.
- Update API CreateClientCertificateWithCsr: add response parameters Body.CertSignBufKmc.


2025-01-21 Version: 1.0.16
- Update API CreateClientCertificate: add param EnableCrl.
- Update API CreateClientCertificate: delete param Csr.
- Update API CreateClientCertificate: update response param.
- Update API CreateClientCertificateWithCsr: add param EnableCrl.
- Update API CreateClientCertificateWithCsr: delete param Csr1.
- Update API CreateClientCertificateWithCsr: update response param.
- Update API CreateCustomCertificate: add param EnableCrl.
- Update API CreateCustomCertificate: update param ApiPassthrough.
- Update API CreateServerCertificate: add param EnableCrl.
- Update API CreateServerCertificate: delete param Csr.
- Update API CreateServerCertificate: update response param.
- Update API CreateServerCertificateWithCsr: add param EnableCrl.
- Update API CreateServerCertificateWithCsr: delete param Csr1.
- Update API CreateServerCertificateWithCsr: update response param.
- Update API CreateSubCACertificate: add param CrlDay.
- Update API CreateSubCACertificate: add param EnableCrl.
- Update API DescribeCACertificate: update response param.
- Update API DescribeCACertificateList: add param Identifier.
- Update API DescribeCACertificateList: update param CurrentPage.
- Update API DescribeCACertificateList: update param ShowSize.
- Update API DescribeCACertificateList: update response param.
- Update API DescribeClientCertificateStatus: update param Identifier.
- Update API GetCAInstanceStatus: add param Identifier.
- Update API GetCAInstanceStatus: update param InstanceId.
- Update API ListClientCertificate: add param Identifier.
- Update API ListClientCertificate: update response param.
- Update API UpdateCACertificateStatus: update param Identifier.
- Update API UpdateCACertificateStatus: update param Status.


2023-03-23 Version: 1.0.15
- Fix some bugs.
- Support PathLenConstraint and ExtendedKeyUsages.

2023-02-13 Version: 1.0.14
- Fix some bugs.

2022-11-29 Version: 1.0.13
- Fix some bugs.

2021-12-23 Version: 0.1.2
- Return the CertificateChain.

2021-11-30 Version: 0.20200630.0
- Publish.

