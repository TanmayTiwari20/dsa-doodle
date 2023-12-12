import requests
import json
import codecs

url = "https://icareconnect--iccqaen.sandbox.my.salesforce.com/services/apexrest/ICC_CopayAPI"

payload = {
    "formSubmittedBy": "Copay Site",
    "lastName": "SmithIICS",
    "identifier": [
        {"type": "TrialCardPatientId", "value": "370862"},
        {"type": "TrialCardEnrollmentId", "value": "958362"},
        {"type": "iCCHubId", "value": ""},
    ],
    "formType": "Copay",
    "communicationLanguage": "",
    "address": {
        "zipCode": "06705",
        "address2": "Lane 1",
        "city": "Waterbury",
        "address1": "12th ave st",
        "addressType": "Home",
        "primaryAddress": True,
        "state": "CT",
    },
    "gender": "M",
    "requestType": "ENROLL",
    "copayVendor": "TrialCard",
    "homePhone": "7878909877",
    "enrollmentDate": "2023-05-31",
    "Practice": {
        "OfficeContactRole": "",
        "Email": "test@test.com",
        "Address": {
            "AddressLine2": "lane 1",
            "AddressLine1": "1 e 2nd st",
            "State": "CT",
            "PostalCode": "06705",
            "Country": "US",
            "City": "Waterbury",
        },
        "PracticeId": "3278108",
        "Phone": {
            "Ext": "",
            "Number": "6786768687",
            "PhoneType": 1,
            "CountryCode": "1",
        },
        "OfficeContactName": "Ins",
        "Fax": {"Ext": "", "Number": "5675757556", "PhoneType": 3, "CountryCode": "1"},
        "Name": "",
    },
    "eligibility": {
        "hasValidPrescription": True,
        "fundedByGov": False,
        "hasCommercialInsurance": True,
        "meetsResidencyReq": True,
        "isMilitary": None,
        "USPrescriber": True,
        "caseOutcome": "Eligible",
    },
    "dateOfBirth": "1990-01-01",
    "consent": {
        "designeeLastName": "",
        "endDate": "2023-05-31T00:00:00.000Z",
        "designeeRelationship": "",
        "permission": "Granted",
        "consentSource": "Website",
        "serviceName": "Commercial Copay",
        "responseDate": "2023-05-31T00:00:00.000Z",
        "eSigned": True,
        "designeeFirstName": "",
        "consentProvidedBy": "",
        "consentType": "Electronic",
        "documentId": "",
        "startDate": "2023-05-31T00:00:00.000Z",
        "consentFormVersion": "MAT-US-2102338-v2.0-09/2021",
    },
    "productName": "Elitek®",
    "firstName": "Quinton",
    "Prescriber": {
        "Specialty": "",
        "Role": "",
        "Suffix": "",
        "Npi": "",
        "FirstName": "Smith",
        "DeaNumber": "",
        "Title": "",
        "TaxIdNumber": "",
        "LastName": "Vince",
        "PrescriberId": "3278107",
        "StateLicenseNumber": "",
    },
    "mobilePhone": "",
    "attachment": None,
    "Pharmacy": None,
    "accountSource": "Website",
    "copay": {
        "initialEnrollmentDate": "2023-01-31T00:00:00",
        "coverageType": "Drug and Infusion",
        "coverageStartDate": "2023-05-31T00:00:00",
        "medical": {
            "bin": "56155",
            "cardId": "500102534",
            "pcn": "",
            "groupNumber": "00003674",
        },
        "eligibleReEnrollmentDate": "2023-12-31T00:00:00",
        "pharmacy": {
            "bin": "610020",
            "cardId": "69089139810",
            "pcn": "",
            "groupNumber": "99994265",
        },
        "coverageEndDate": "2023-12-31T00:00:00",
    },
    "email": "Dinesh.s@sanofi.com",
}
headers = {
    "Authorization": "Bearer 00D020000008oJO!ARkAQG0m7BlGMm5ufKiJKDMKyRVeugbHBjvm0uHlb.P93H_7QKScUDzNY9Slj0gV5KGCrhpUDDH.I072Glld1WW5yDbdmdjc",
    "Content-Type": "application/json",
    "Cookie": "BrowserId=MwU9rsxzEe2S-QemwNTRJA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1",
}

encoded_payload = json.dumps(payload, ensure_ascii=False)

print(encoded_payload)

response = requests.post(url, headers=headers, data=encoded_payload.encode("utf-8"))

print(response.text)
