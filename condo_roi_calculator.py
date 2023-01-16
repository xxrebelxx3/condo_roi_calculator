# variables
condo_cost = 250_000
nightly_rent = 200
cleaning_fee = 20
closing_pct = 8
yearly_tax = 2
property_mgmt_pct = 10
listing_pct = 10
occupancy_rate = 80
insurance_yearly = 2000
company_formation = 5000

yearly_rev = nightly_rent * 365 * (occupancy_rate / 100)

yearly_cost = (cleaning_fee * 365 * (occupancy_rate / 100)) + (condo_cost * (yearly_tax / 100)) + ((nightly_rent * (property_mgmt_pct / 100)) + (nightly_rent * (listing_pct / 100)) * 365 * (occupancy_rate / 100)) + insurance_yearly

final_cost = condo_cost + (condo_cost * closing_pct / 100) + company_formation

yearly_net = yearly_rev - yearly_cost

yearly_roi_pct = yearly_net / final_cost * 100

roi = final_cost / yearly_net

print("final cost: ", final_cost)
print("yearly roi: ", yearly_roi_pct)
print("years until roi: ", roi)



