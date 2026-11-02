# Agent roster: agentic-a2a-protocol

_Cross-organization agents talking over the A2A protocol_


## 1. Freight Marketplace (`apps/app01_freight_marketplace.py`)

Task: Ship 12 pallets from Rotterdam to Milan within 4 days.

- **Shipper Agent** (`shipper_agent`): Post the shipment request.
- **Carrier Agent** (`carrier_agent`): Bid with rates.
- **Customs Agent** (`customs_agent`): Pre-clear documents.
- **Insurance Agent** (`insurance_agent`): Quote cargo cover.
- **Tracking Agent** (`tracking_agent`): Provide tracking plan.

## 2. Airline-Hotel-Car Alliance (`apps/app02_travel_alliance.py`)

Task: Book a business trip bundle across three companies.

- **Airline Agent** (`airline_agent`): Offer flights.
- **Hotel Agent** (`hotel_agent`): Offer rooms.
- **Car Rental Agent** (`car_rental_agent`): Offer vehicles.
- **Bundler Agent** (`bundler_agent`): Combine offers.
- **Payment Agent** (`payment_agent`): Split payment.

## 3. Hospital Referral Network (educational) (`apps/app03_healthcare_referral.py`)

Task: Refer a patient between a clinic, lab and specialist.

- **Clinic Agent** (`clinic_agent`): Create referral.
- **Lab Agent** (`lab_agent`): Schedule tests.
- **Specialist Agent** (`specialist_agent`): Propose appointment.
- **Insurance Agent** (`insurance_agent`): Check authorization.
- **Patient Liaison Agent** (`patient_liaison_agent`): Notify patient.

## 4. Smart Grid Negotiation (`apps/app04_smart_grid.py`)

Task: Balance a neighborhood's solar surplus and EV charging.

- **Household Agent** (`household_agent`): Report demand.
- **Solar Producer Agent** (`solar_producer_agent`): Offer surplus.
- **Battery Agent** (`battery_agent`): Offer storage.
- **Grid Operator Agent** (`grid_operator_agent`): Set limits.
- **Billing Agent** (`billing_agent`): Settle prices.

## 5. Cross-Journal Peer Review (`apps/app05_academic_peer_review.py`)

Task: Coordinate review of a manuscript across two journals.

- **Editor Agent** (`editor_agent`): Assign reviewers.
- **Reviewer Agent** (`reviewer_agent`): Write review.
- **Plagiarism Agent** (`plagiarism_agent`): Similarity check.
- **Ethics Agent** (`ethics_agent`): Ethics check.
- **Decision Agent** (`decision_agent`): Summarize decision.

## 6. Real Estate Closing Network (`apps/app06_real_estate_closing.py`)

Task: Close a home sale among buyer, seller, bank and title company.

- **Buyer Agent** (`buyer_agent`): Submit offer terms.
- **Seller Agent** (`seller_agent`): Respond to terms.
- **Bank Agent** (`bank_agent`): Confirm financing.
- **Title Agent** (`title_agent`): Confirm title.
- **Escrow Agent** (`escrow_agent`): Schedule closing.

## 7. Food Delivery Mesh (`apps/app07_food_delivery_mesh.py`)

Task: Order dinner from two restaurants with one courier.

- **Customer Agent** (`customer_agent`): Place order.
- **Restaurant Agent** (`restaurant_agent`): Confirm menu and time.
- **Courier Agent** (`courier_agent`): Plan pickup.
- **Payment Agent** (`payment_agent`): Authorize payment.
- **Support Agent** (`support_agent`): Handle issues.

## 8. Recruitment Exchange (`apps/app08_recruitment_exchange.py`)

Task: Match a candidate pool from an agency to an employer.

- **Employer Agent** (`employer_agent`): Post requirements.
- **Agency Agent** (`agency_agent`): Present candidates.
- **Background Check Agent** (`background_check_agent`): Verify claims.
- **Scheduling Agent** (`scheduling_agent`): Arrange interviews.
- **Offer Agent** (`offer_agent`): Negotiate offer.

## 9. Relief Supply Exchange (`apps/app09_disaster_relief_exchange.py`)

Task: Match donor offers to shelter needs after an earthquake.

- **Needs Agent** (`needs_agent`): Publish needs.
- **Donor Agent** (`donor_agent`): Publish offers.
- **Logistics Agent** (`logistics_agent`): Plan transport.
- **Verification Agent** (`verification_agent`): Verify requests.
- **Reporting Agent** (`reporting_agent`): Publish transparency report.

## 10. Conference Federation (`apps/app10_conference_federation.py`)

Task: Merge schedules from three co-located conferences.

- **Organizer Agent** (`organizer_agent`): Publish sessions.
- **Speaker Agent** (`speaker_agent`): Confirm availability.
- **Room Agent** (`room_agent`): Allocate rooms.
- **Attendee Agent** (`attendee_agent`): Build personal agenda.
- **Conflict Resolver Agent** (`conflict_resolver_agent`): Resolve clashes.

## 11. Reinsurance Placement (`apps/app11_insurance_reinsurance.py`)

Task: Place a risk with two reinsurers.

- **Broker Agent** (`broker_agent`): Present the risk.
- **Primary Insurer Agent** (`primary_insurer_agent`): Describe retention.
- **Reinsurer A Agent** (`reinsurer_a_agent`): Quote.
- **Reinsurer B Agent** (`reinsurer_b_agent`): Quote.
- **Compliance Agent** (`compliance_agent`): Check regulations.
