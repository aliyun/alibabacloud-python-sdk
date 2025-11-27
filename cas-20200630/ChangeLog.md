2025-11-27 Version: 1.2.4
- Update API DescribeCACertificate: add response parameters Body.Certificate.ClusterId.
- Update API DescribeCACertificate: add response parameters Body.Certificate.KeyIndex.


2025-10-31 Version: 1.2.3
- Generated python 2020-06-30 for cas.

2025-10-30 Version: 1.2.2
- Update API CreateClientCertificate: add request parameters ResourceGroupId.
- Update API CreateClientCertificate: add request parameters Tags.
- Update API CreateClientCertificateWithCsr: add request parameters ResourceGroupId.
- Update API CreateClientCertificateWithCsr: add request parameters Tags.
- Update API CreateCustomCertificate: add request parameters ResourceGroupId.
- Update API CreateCustomCertificate: add request parameters Tags.
- Update API CreateExternalCACertificate: add request parameters ResourceGroupId.
- Update API CreateExternalCACertificate: add request parameters Tags.
- Update API CreateRootCACertificate: add request parameters ResourceGroupId.
- Update API CreateRootCACertificate: add request parameters Tags.
- Update API CreateServerCertificate: add request parameters ResourceGroupId.
- Update API CreateServerCertificate: add request parameters Tags.
- Update API CreateServerCertificateWithCsr: add request parameters ResourceGroupId.
- Update API CreateServerCertificateWithCsr: add request parameters Tags.
- Update API CreateSubCACertificate: add request parameters ClientToken.
- Update API CreateSubCACertificate: add request parameters ResourceGroupId.
- Update API CreateSubCACertificate: add request parameters Tags.
- Update API DescribeCACertificate: add response parameters Body.Certificate.ResourceGroupId.
- Update API DescribeCACertificate: add response parameters Body.Certificate.Tags.
- Update API DescribeCACertificateList: add request parameters ResourceGroupId.
- Update API DescribeCACertificateList: add response parameters Body.CertificateList.$.ResourceGroupId.
- Update API DescribeClientCertificate: add response parameters Body.Certificate.ResourceGroupId.
- Update API DescribeClientCertificate: add response parameters Body.Certificate.Tags.
- Update API ListClientCertificate: add request parameters ResourceGroupId.
- Update API ListClientCertificate: add response parameters Body.CertificateList.$.ResourceGroupId.


2025-09-17 Version: 1.2.1
- Generated python 2020-06-30 for cas.

2025-09-12 Version: 1.2.0
- Support API CreateExternalCACertificate.
- Support API ListPcaCaCertificate.


2025-08-18 Version: 1.1.6
- Generated python 2020-06-30 for cas.

2025-08-07 Version: 1.1.5
- Generated python 2020-06-30 for cas.

2025-07-30 Version: 1.1.4
- Update API CreateRootCACertificate: add request parameters ClientToken.
- Update API DescribeCACertificate: add response parameters Body.Certificate.FullAlgorithm.
- Update API DescribeCACertificate: add response parameters Body.Certificate.IssuerType.
- Update API DescribeCACertificate: add response parameters Body.Certificate.Years.
- Update API UpdateCACertificateStatus: add request parameters ClientToken.


2025-07-30 Version: 1.1.4
- Update API CreateRootCACertificate: add request parameters ClientToken.
- Update API DescribeCACertificate: add response parameters Body.Certificate.FullAlgorithm.
- Update API DescribeCACertificate: add response parameters Body.Certificate.IssuerType.
- Update API DescribeCACertificate: add response parameters Body.Certificate.Years.
- Update API UpdateCACertificateStatus: add request parameters ClientToken.


2025-07-30 Version: 1.1.4
- Update API CreateRootCACertificate: add request parameters ClientToken.
- Update API DescribeCACertificate: add response parameters Body.Certificate.FullAlgorithm.
- Update API DescribeCACertificate: add response parameters Body.Certificate.IssuerType.
- Update API DescribeCACertificate: add response parameters Body.Certificate.Years.
- Update API UpdateCACertificateStatus: add request parameters ClientToken.


2025-07-02 Version: 1.1.3
- Generated python 2020-06-30 for cas.

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

