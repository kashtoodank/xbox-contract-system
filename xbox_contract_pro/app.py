<h1>XBOX ACCOUNT RENTAL AGREEMENT</h1>
 
Date: <strong>{{ current_date }}</strong><p>
This Xbox Account Rental Agreement ("Agreement") is between:
</p>

<p>
Account Owner: <strong>elucd</strong>
</p>

<p>
and
</p>

<p>
Renter:
<input type="text" name="full_name" required>
</p>

<h2>1. Rental Account</h2>

<p>
The Account Owner agrees to provide the Renter temporary access to an Xbox account for the rental period stated below.
</p>

<p>
Rental Period: 5 Days<br>
Rental Price: $5.00<br>
Security Deposit: None
</p>

<p>
The rental begins on <strong>8/10/26</strong> and ends on <strong>8/15/26</strong>.
</p>

<h2>2. Permitted Use</h2>

<p>
The Renter may use the Xbox account only for their personal use during the rental period.
</p>

<p>
The Renter may make changes to in-game accessories, cosmetic items, animations, or other permitted in-game customization.
</p>

<h2>3. Account Information</h2>

<p>
The Renter must not change, remove, add, or modify any account information or security settings.
</p>

<p>This includes, but is not limited to:</p>

<ul>
<li>Password</li>
<li>Email address</li>
<li>Phone number</li>
<li>Security information</li>
<li>Account recovery information</li>
<li>Account ownership information</li>
<li>Privacy or security settings</li>
</ul>

<p>
The account must be returned and maintained in the same condition in which it was provided, except for permitted in-game changes.
</p>

<h2>4. Account Access</h2>

<p>
Only the person who rented the account may use the account during the rental period.
</p>

<p>The Renter may not:</p>

<ul>
<li>Share the account with another person</li>
<li>Sell or rent the account to someone else</li>
<li>Give another person access to the account</li>
<li>Attempt to claim ownership of the account</li>
<li>Lock the Account Owner out of the account</li>
</ul>

<h2>5. Breach of Agreement</h2>

<p>
If the Renter violates any term of this Agreement, the Account Owner may immediately terminate the rental and take reasonable legal action available under applicable law.
</p>

<p>
If the Renter causes financial loss, damage, unauthorized changes, or other harm to the Account Owner, the Renter may be responsible for legally recoverable damages, costs, or other remedies.
</p>

<p>
Any penalty or fee must comply with applicable law and cannot be imposed merely because it is written in this Agreement.
</p>

<h2>6. Return of Access</h2>

<p>
When the five-day rental period ends, the Renter must stop using the account and must not attempt to access it again unless the Account Owner provides additional authorization.
</p>

<h2>7. No Ownership Transfer</h2>

<p>
This Agreement grants temporary use of the account only. It does not transfer ownership of the Xbox account to the Renter.
</p>

<h2>8. Platform Rules</h2>

<p>
The parties understand that Xbox/Microsoft may have separate rules governing Xbox accounts and account access. Nothing in this Agreement requires either party to violate those rules.
</p>

<h2>9. Agreement</h2>

<p>
By signing below, both parties confirm that they have read, understood, and agreed to the terms of this Agreement.
</p>

<p>
Account Owner Signature: <strong>elucd</strong>
</p>

<p>
Date: <strong>{{ current_date }}</strong>                                                                                                         
 </p>      
<hr>
<h3>Renter Information</h3>

<label>Payhip Order ID</label><br>
<input type="text" name="order_id" required>

<br><br>

<label>Renter First and Last Name</label><br>
<input type="text" name="legal_name" required>

<br><br>

<label>Email Address</label><br>
<input type="email" name="email" required>

<br><br>

<label>Phone Number (Optional)</label><br>
<input type="text" name="phone">

<br><br>

<label>Type Your Full Name as Signature</label><br>
<input type="text" name="typed_signature" required>

<br><br>

<label>Draw Signature Below</label><br>

<canvas id="signature-pad" width="600" height="200"></canvas>

<input type="hidden"
       id="signature_data"
       name="signature_data">

<br><br>

<label>
<input type="checkbox" required>
I have read, understood, and agree to this Xbox Account Rental Agreement.
</label>

<br><br>

<button type="submit">
Submit Agreement
</button>
